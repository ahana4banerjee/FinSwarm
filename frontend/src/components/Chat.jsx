import { useState } from "react";

export default function Chat({ onInsight }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = {
      role: "user",
      content: input,
    };

    setMessages((prev) => [...prev, userMessage]);

    const res = await fetch("http://localhost:7071/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });

    const data = await res.json();

    const botMessage = {
      role: "assistant",
      content: data.answer,
    };

    setMessages((prev) => [...prev, botMessage]);
    setInput("");

    // 🔑 pass proactive insight to right panel
    onInsight(data.proactive_insight);
  };

  return (
    <>
      <div style={chatBox}>
        {messages.map((m, i) => (
          <div
            key={i}
            style={{
              alignSelf: m.role === "user" ? "flex-end" : "flex-start",
              background: m.role === "user" ? "#2563eb" : "#020617",
              color: "#e5e7eb",
              padding: "10px",
              borderRadius: "8px",
              marginBottom: "8px",
              maxWidth: "70%",
              whiteSpace: "pre-line", // IMPORTANT
            }}
          >
            {m.content}
          </div>
        ))}
      </div>

      <div style={inputRow}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question..."
          style={inputStyle}
        />
        <button onClick={sendMessage} style={sendBtn}>
          Send
        </button>
      </div>
    </>
  );
}

/* styles */
const chatBox = {
  flex: 1,
  display: "flex",
  flexDirection: "column",
  overflowY: "auto",
  marginBottom: "12px",
};

const inputRow = {
  display: "flex",
  gap: "8px",
};

const inputStyle = {
  flex: 1,
  padding: "10px",
  borderRadius: "6px",
  border: "1px solid #334155",
  background: "#020617",
  color: "#e5e7eb",
};

const sendBtn = {
  padding: "10px 16px",
  borderRadius: "6px",
  border: "none",
  background: "#2563eb",
  color: "white",
  cursor: "pointer",
};
