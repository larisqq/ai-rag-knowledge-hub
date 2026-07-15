import { useState } from "react";

import { api } from "../services/api";

import type { ChatResponse } from "../types/chat";

export default function ChatBox() {
  const [question, setQuestion] = useState("");

  const [response, setResponse] = useState<ChatResponse | null>(null);

  const [loading, setLoading] = useState(false);

  async function askQuestion() {
    if (!question.trim()) {
      return;
    }

    setLoading(true);

    try {
      const result = await api.post<ChatResponse>("/chat", {
        question,
      });

      setResponse(result.data);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <h2>Ask AI</h2>

      <input
        type="text"
        value={question}
        placeholder="Ask a question..."
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={askQuestion} disabled={loading}>
        {loading ? "Thinking..." : "Ask"}
      </button>

      {response && (
        <div>
          <h3>Answer</h3>

          <p>{response.answer}</p>

          {response.sources.length > 0 && (
            <>
              <h3>Sources</h3>

              <ul>
                {response.sources.map((source) => (
                  <li key={`${source.filename}-${source.chunk_index}`}>
                    {source.filename} (chunk {source.chunk_index})
                  </li>
                ))}
              </ul>
            </>
          )}
        </div>
      )}
    </div>
  );
}
