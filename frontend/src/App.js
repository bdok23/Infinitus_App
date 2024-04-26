import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleAskQuestion = async () => {
    setIsLoading(true);
    console.log(`Asking question: ${question}`); // Log the question being asked
    try {
      const response = await axios.post('http://localhost:5000/ask', { question });
      console.log(`Received answer: ${response.data.answer}`); // Log the answer received
      setAnswer(response.data.answer);
    } catch (error) {
      console.error('Error fetching the answer:', error);
      setAnswer('Failed to fetch answer');
    }
    setIsLoading(false);
  };

  return (
    <div>
      <input type="text" value={question} onChange={(e) => setQuestion(e.target.value)} />
      <button onClick={handleAskQuestion} disabled={!question.trim() || isLoading}>
        Ask
      </button>
      {isLoading ? <p>Loading...</p> : <p>Answer: {answer}</p>}
    </div>
  );
}

export default App;
