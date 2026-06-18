import { useState } from "react";
import axios from "axios";

function App() {

  const [question, setQuestion] = useState("");
  const [file, setFile] = useState(null);
  const [uploadMessage, setUploadMessage] = useState("");

  const [chatHistory, setChatHistory] = useState([]);

  const API = "http://13.60.179.121:8000";

  const uploadFile = async () => {

    if (!file) {
      alert("Please select a PDF");
      return;
    }

    const formData = new FormData();

    formData.append(
      "file",
      file
    );

    try {

      const response =
        await axios.post(
          API + "/upload",
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

    if (!question.trim()) {
      return;
    }

    try {

      const response =
        await axios.post(
          API +
          "/ask?question=" +
          encodeURIComponent(question)
        );

      const newChat = {
        question: question,
        answer: response.data.answer,
        sources:
          response.data.sources || []
      };

      setChatHistory(
        (prev) => [...prev, newChat]
      );

      setQuestion("");

    } catch (error) {

      console.error(error);

      alert(
        "Backend connection failed"
      );
    }
  };

  return (

    <div
      style={{
        padding: "30px",
        maxWidth: "1000px",
        margin: "auto",
        fontFamily: "Arial"
      }}
    >

      <h1>
        📚 RAG Chatbot
      </h1>

      <hr />

      <h2>
        Upload PDF
      </h2>

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
          marginLeft: "10px"
        }}
      >
        Upload
      </button>

      <p>
        {uploadMessage}
      </p>

      <hr />

      <h2>
        Ask Question
      </h2>

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
          width: "600px",
          padding: "10px"
        }}
      />

      <button
        onClick={askQuestion}
        style={{
          marginLeft: "10px"
        }}
      >
        Ask
      </button>

      <hr />

      <h2>
        Conversation History
      </h2>

      {chatHistory.map(
        (chat, index) => (

          <div
            key={index}
            style={{
              border: "1px solid #ccc",
              padding: "15px",
              marginBottom: "15px",
              borderRadius: "10px"
            }}
          >

            <h3>
              🙋 Question
            </h3>

            <p>
              {chat.question}
            </p>

            <h3>
              🤖 Answer
            </h3>

            <p>
              {chat.answer}
            </p>

            <h4>
              📄 Source PDFs
            </h4>

            {chat.sources.length > 0 ? (

              <ul>
                {chat.sources.map(
                  (source, i) => (
                    <li key={i}>
                      {source}
                    </li>
                  )
                )}
              </ul>

            ) : (

              <p>
                No source information
              </p>

            )}

          </div>
        )
      )}

    </div>
  );
}

export default App;
