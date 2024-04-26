from flask import Flask, request, jsonify
from llm_integration import answer_question
from flask_cors import CORS  # Ensure CORS is handled
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes
logging.basicConfig(level=logging.DEBUG)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data['question']
    logging.debug(f"Received question: {question}")
    answer = answer_question(question)
    logging.debug(f"Generated answer: {answer}")
    return jsonify(answer=answer)

if __name__ == '__main__':
    app.run(debug=False, port=5000)
