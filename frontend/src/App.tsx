import { useState } from "react";
import "./index.css";
import InputForm from "./components/InputForm";
import GraphView from "./components/GraphView";

function App() {
  const [data, setData] = useState<any>(null);

  return (
    <div className="container">
      <h1>📚 Gutenberg Book Analyzer</h1>
      <InputForm onResult={setData} />
      {data && (
        <>
          <h2>📊 Character Interaction Graph</h2>
          <GraphView data={data} />

          <h2>🧾 Raw Analysis Result</h2>
          <pre style={{ background: "#eee", padding: "1rem", overflowX: "auto" }}>
            {JSON.stringify(data, null, 2)}
          </pre>
        </>
      )}
    </div>
  );
}

export default App;
