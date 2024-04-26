import pdfplumber
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
import logging

PDF_PATH = 'document.pdf'
tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", index_name="exact", use_dummy_dataset=True)
model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq", retriever=retriever)

def extract_text_from_pdf():
    text = ""
    with pdfplumber.open(PDF_PATH) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + '\n'
    return text

def answer_question(question):
    context = extract_text_from_pdf()
    logging.debug(f"Extracted context: {context[:500]}")  # Log the first 500 characters of the context
    inputs = tokenizer(question, context, return_tensors="pt", truncation=True, max_length=512)
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']
    logging.debug(f"Tokenized inputs: {inputs}")
    output = model.generate(input_ids=input_ids, attention_mask=attention_mask, max_length=50)
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    logging.debug(f"Generated answer: {answer}")
    return answer
