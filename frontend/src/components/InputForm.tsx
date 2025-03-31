import { useState } from "react";
import axios from "axios";

export default function InputForm({ onResult }: any) {
    const [bookId, setBookId] = useState("");
    const [bookText, setBookText] = useState("");

    const fetchData = async () => {
        const res = await axios.get(`http://localhost:8000/analyze/${bookId}`);
        onResult(res.data);
        console.log("Data in InputForm component:",res.data);
    };

    const fetchBookText = async () => {
        const res = await axios.get(`http://localhost:8000/book/${bookId}`);
        setBookText(res.data.text); // Save it in state
    };

    return (
        <div>
            <div style={{ marginBottom: "20px" }}>
                <input
                    type="text"
                    placeholder="Enter Book ID"
                    value={bookId}
                    onChange={(e) => setBookId(e.target.value)}
                />
                <button onClick={fetchData}>Analyze</button>
                <span style={{ margin: "0 10px" }}></span>
                <button onClick={fetchBookText}> Show the Book Content </button>
            </div>
            <div>
                <pre style={{ whiteSpace: 'pre-wrap', maxHeight: '400px', overflowY: 'scroll' }}>
                    {bookText}
                </pre>

            </div>
        </div>
    );
}
