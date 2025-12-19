import { useState } from "react";

export default function Roadmap({ roadmap, units, currentPhase }) {
  const [activeUnit, setActiveUnit] = useState(null);

  return (
    <div>
      <h3 style={{ marginBottom: "12px" }}>Learning Roadmap</h3>

      {roadmap.map((phase) => {
        const isActive = phase.phase === currentPhase;

        return (
          <div
            key={phase.phase}
            style={{
              ...phaseCard,
              border: isActive
                ? "1px solid #2563eb"
                : "1px solid #1e293b",
            }}
          >
            <div style={{ fontWeight: "600", marginBottom: "6px" }}>
              Phase {phase.phase}: {phase.title}
              {isActive && <span style={badge}>CURRENT</span>}
            </div>

            {/* Units under each phase */}
            {units
              .filter((u) => u.phase === phase.phase)
              .map((unit) => (
                <div
                  key={unit.unit_id}
                  onClick={() => setActiveUnit(unit)}
                  style={unitItem}
                >
                  ▸ {unit.title}
                </div>
              ))}
          </div>
        );
      })}

      {/* Learning Card */}
      {activeUnit && (
        <div style={learningCard}>
          <h4 style={{ marginBottom: "6px" }}>{activeUnit.title}</h4>
          <p style={{ fontSize: "14px", color: "#cbd5f5" }}>
            Click the chat to ask questions about this unit.
          </p>
          <p style={{ fontSize: "12px", marginTop: "8px", color: "#94a3b8" }}>
            Source: RBI / SEBI curated content
          </p>
        </div>
      )}
    </div>
  );
}

/* styles */
const phaseCard = {
  padding: "10px",
  borderRadius: "8px",
  marginBottom: "10px",
  background: "#020617",
};

const unitItem = {
  fontSize: "14px",
  color: "#cbd5f5",
  paddingLeft: "10px",
  cursor: "pointer",
  marginBottom: "4px",
};

const learningCard = {
  marginTop: "16px",
  padding: "12px",
  borderRadius: "8px",
  background: "#020617",
  border: "1px solid #2563eb",
};

const badge = {
  marginLeft: "6px",
  fontSize: "11px",
  padding: "2px 6px",
  background: "#2563eb",
  borderRadius: "4px",
};
