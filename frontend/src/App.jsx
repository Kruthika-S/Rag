import { useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const [file, setFile] = useState(null);
  const [uploadMessage, setUploadMessage] =
    useState("");

  const uploadFile = async () => {
    if (!file) {
      alert("Please select a PDF");
      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://56.228.27.39:8000/upload",
        formData
      );

      setUploadMessage(
        response.data.message
      );
    } catch (error) {
      console.error(error);

      setUploadMessage(
        "Upload failed"
      );
    }
  };

  const askQuestion = async () => {
    try {
      const response = await axios.post(
        `http://56.228.27.39:8000/ask?question=${question}`
      );

      setAnswer(
        response.data.answer
      );
    } catch (error) {
      console.error(error);

      setAnswer(
        "Error getting answer"
      );
    }
  };

  return (
    <div
      style={{
        padding: "30px",
        fontFamily: "Arial",
      }}
    >
      <h1>📚 RAG Chatbot</h1>

      <hr />

      <h2>Upload PDF</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) =>
          setFile(
            e.target.files[0]
          )
        }
      />

      <button
        onClick={uploadFile}
        style={{
          marginLeft: "10px",
        }}
      >
        Upload Document
      </button>

      <p>
        {uploadMessage}
      </p>

      <hr />

      <h2>Ask Question</h2>

      <input
        type="text"
        value={question}
        onChange={(e) =>
          setQuestion(
            e.target.value
          )
        }
        placeholder="Ask a question..."
        style={{
          width: "500px",
          padding: "8px",
        }}
      />

      <button
        onClick={askQuestion}
        style={{
          marginLeft: "10px",
        }}
      >
        Ask
      </button>

      <h3>Answer</h3>

      <div
        style={{
          border: "1px solid #ccc",
          padding: "15px",
          borderRadius: "8px",
          maxWidth: "800px",
        }}
      >
        {answer}
      </div>
    </div>
  );
}

export default App;
