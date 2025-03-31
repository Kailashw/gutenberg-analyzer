import { useState } from "react";
import InputForm from "./components/InputForm";
import GraphView from "./components/GraphView";

function App() {
  const [data, setData] = useState<any | null>(null);

  return (
    <div className="container">
      <h1>📚 Gutenberg Book Analyzer</h1>
      <InputForm onResult={setData} />
      {data && (
        <>
          <h2>🕸️ Character Interaction Graph</h2>
          <GraphView data={data} />
        </>
      )}
    </div>
  );
}

export default App;
