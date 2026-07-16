import type { Message } from "../../types/message";

import "./MessageBubble.css";

interface Props {
  message: Message;
}

export default function MessageBubble({ message }: Props) {
  const isUser = message.role === "user";

  const isThinking =
    message.role === "assistant" && message.content === "Thinking...";

  return (
    <div className={`message ${isUser ? "user" : "assistant"}`}>
      <div className="message-header">{isUser ? "👤 You" : "🤖 AI"}</div>

      <div className="message-content">
        {isThinking ? (
          <span className="typing">
            <span></span>
            <span></span>
            <span></span>
          </span>
        ) : (
          message.content
        )}
      </div>

      {!isThinking && message.sources && message.sources.length > 0 && (
        <div className="sources">
          <strong>Sources</strong>

          <ul>
            {message.sources.map((source) => (
              <li key={`${source.filename}-${source.chunk_index}`}>
                📄 {source.filename} (chunk {source.chunk_index})
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
