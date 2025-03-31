import { useState } from "react";
import InputForm from "./components/InputForm";
import GraphView from "./components/GraphView";

function App() {
  const [data, setData] = useState<any | null>(null);
  console.log("Data in App component:", data);
  return (
    <div className="container">
      <h1>📚 Gutenberg Book Analyzer</h1>
      <InputForm onResult={setData} />
      {data && data?.length === 0 && (
        <h2 style={{ color: "red" }}>
          No data available. Please upload a book file to analyze.
        </h2>
      )}
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
