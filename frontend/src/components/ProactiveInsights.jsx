export default function ProactiveInsights({ insight }) {
  if (!insight) {
    return (
      <div>
        <h3 style={{ marginBottom: "12px" }}>Insights for You</h3>
        <div style={card}>
          <p style={{ fontSize: "14px", color: "#cbd5f5" }}>
            No new insights yet.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div>
      <h3 style={{ marginBottom: "12px" }}>Insights for You</h3>

      <div style={card}>
        <div style={{ fontSize: "12px", color: "#60a5fa", marginBottom: "6px" }}>
          {insight.type?.toUpperCase()}
        </div>

        <p style={{ marginBottom: "8px" }}>{insight.message}</p>

        <p style={{ fontSize: "14px", color: "#cbd5f5" }}>
          <strong>Next:</strong> {insight.suggestion}
        </p>

        <p style={{ fontSize: "12px", color: "#94a3b8", marginTop: "8px" }}>
          Source: {insight.source}
        </p>
      </div>
    </div>
  );
}

const card = {
  background: "#020617",
  padding: "12px",
  borderRadius: "8px",
  border: "1px solid #1e293b",
};
