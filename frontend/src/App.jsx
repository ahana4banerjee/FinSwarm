import { useState } from "react";
import GoalSetup from "./components/GoalSetup";
import Dashboard from "./pages/Dashboard";

function App() {
  const [goalData, setGoalData] = useState(null);

  return (
    <>
      {!goalData ? (
        <GoalSetup onGoalSet={setGoalData} />
      ) : (
        <Dashboard goalData={goalData} />
      )}
    </>
  );
}

export default App;
