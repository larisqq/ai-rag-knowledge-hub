import { useEffect, useRef, useState } from "react";

import { api } from "../../services/api";

import type { ChatResponse } from "../../types/chat";
import type { Message } from "../../types/message";

import Card from "../Card/Card";
import MessageBubble from "../MessageBubble/MessageBubble";

import "./ChatBox.css";

export default function ChatBox() {
  const [question, setQuestion] = useState("");

  const [messages, setMessages] = useState<Message[]>([]);

  const [loading, setLoading] = useState(false);

  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  async function askQuestion() {
    if (!question.trim() || loading) {
      return;
    }

    const currentQuestion = question.trim();

    setQuestion("");

    const userMessage: Message = {
      id: crypto.randomUUID(),
      role: "user",
      content: currentQuestion,
    };

    setMessages((previous) => [...previous, userMessage]);

    setLoading(true);

    try {
      const { data } = await api.post<ChatResponse>("/chat", {
        question: currentQuestion,
      });

      const assistantMessage: Message = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: data.answer,
        sources: data.sources,
      };

      setMessages((previous) => [...previous, assistantMessage]);
    } catch (error) {
      console.error(error);

      const errorMessage: Message = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: "Sorry, something went wrong.",
      };

      setMessages((previous) => [...previous, errorMessage]);
    } finally {
      setLoading(false);
    }
  }

  function clearChat() {
    setMessages([]);
  }
  return (
    <Card title="Ask AI">
      <div className="chat-history">
        {messages.map((message, index) => (
          <MessageBubble key={index} message={message} />
        ))}

        <div ref={bottomRef} />
      </div>

      <div className="chat-input">
        <input
          type="text"
          value={question}
          placeholder="Ask a question..."
          onChange={(event) => setQuestion(event.target.value)}
          onKeyDown={(event) => {
            if (event.key === "Enter") {
              askQuestion();
            }
          }}
        />

        <button onClick={askQuestion} disabled={loading || !question.trim()}>
          {loading ? "Thinking..." : "Ask"}
        </button>

        <button onClick={clearChat} disabled={messages.length === 0}>
          Clear
        </button>
      </div>
    </Card>
  );
}
