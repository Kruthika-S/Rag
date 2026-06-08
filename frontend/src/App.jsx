import { useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askQuestion = async () => {
    const response = await axios.post(
      `http://56.228.27.39:8000/ask?question=${question}`
    );

    setAnswer(response.data.answer);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>RAG Chatbot</h1>

      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask a question..."
        style={{ width: "400px" }}
      />

      <button onClick={askQuestion}>
        Ask
      </button>

      <p>{answer}</p>
    </div>
  );
}

export default App;
