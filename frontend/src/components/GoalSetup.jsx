import { useState } from "react";

export default function GoalSetup({ onGoalSet }) {
  const [goal, setGoal] = useState("");
  const [duration, setDuration] = useState("");

  const submitGoal = async () => {
    const res = await fetch("http://localhost:7071/api/goal", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ goal, duration }),
    });

    const data = await res.json();
    onGoalSet(data);
  };

  const inputStyle = {
  width: "100%",
  padding: "10px",
  marginBottom: "12px",
  borderRadius: "6px",
  border: "1px solid #334155",
  background: "#020617",
  color: "#e5e7eb"
};

const buttonStyle = {
  width: "100%",
  padding: "10px",
  borderRadius: "6px",
  border: "none",
  background: "#2563eb",
  color: "white",
  fontWeight: "600",
  cursor: "pointer"
};


 return (
  <div style={{
    minHeight: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center"
  }}>
    <div style={{
      width: "420px",
      padding: "32px",
      background: "#020617",
      borderRadius: "12px",
      boxShadow: "0 10px 30px rgba(0,0,0,0.5)"
    }}>
      <h2 style={{ marginBottom: "20px" }}>Set your learning goal</h2>

      <input
        placeholder="Your goal (e.g. Learn personal finance)"
        value={goal}
        onChange={(e) => setGoal(e.target.value)}
        style={inputStyle}
      />

      <input
        placeholder="Duration (e.g. 2 months)"
        value={duration}
        onChange={(e) => setDuration(e.target.value)}
        style={inputStyle}
      />

      <button
        onClick={submitGoal}
        style={buttonStyle}
      >
        Start Learning
      </button>
    </div>
  </div>
);
}