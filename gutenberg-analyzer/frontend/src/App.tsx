import { useState } from "react";
import InputForm from "./components/InputForm";
import GraphView from "./components/GraphView";
import "../src/index.css";

function App() {
  const [data, setData] = useState(null);

  return (
    <div className="container">
      <h1>📚 Gutenberg Book Analyzer</h1>
      <InputForm onResult={setData} />
      {data && <GraphView data={data} />}
    </div>
  );
}

export default App;
