import { useState } from "react";
import Roadmap from "../components/Roadmap";
import Chat from "../components/Chat";
import ProactiveInsights from "../components/ProactiveInsights";


export default function Dashboard({ goalData }) {
  const [insight, setInsight] = useState(null);

  return (
    <div style={container}>
      <div style={left}>
        <Roadmap
            roadmap={goalData.roadmap.roadmap}
            units={goalData.learning_state.all_units}
            currentPhase={goalData.learning_state.current_unit.phase}
        />

      </div>

      <div style={center}>
        <Chat onInsight={setInsight} />
      </div>

      <div style={right}>
        <ProactiveInsights insight={insight} />
      </div>
    </div>
  );
}

/* styles */
const container = {
  display: "flex",
  height: "100vh",
  background: "#0f172a",
};

const left = {
  width: "22%",
  borderRight: "1px solid #1e293b",
  padding: "16px",
  overflowY: "auto",
};

const center = {
  width: "56%",
  padding: "16px",
  borderRight: "1px solid #1e293b",
  display: "flex",
  flexDirection: "column",
};

const right = {
  width: "22%",
  padding: "16px",
  background: "#020617",
};
