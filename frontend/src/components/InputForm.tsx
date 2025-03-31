import { useState } from "react";
import axios from "axios";

export default function InputForm({ onResult }: any) {
    const [bookId, setBookId] = useState("");

    const fetchData = async () => {
        const res = await axios.get(`http://localhost:8000/analyze/${bookId}`);
        onResult(JSON.parse(res.data));
    };

    return (
        <div style={{ marginBottom: "20px" }}>
            <input
                type="text"
                placeholder="Enter Book ID"
                value={bookId}
                onChange={(e) => setBookId(e.target.value)}
            />
            <button onClick={fetchData}>Analyze</button>
        </div>
    );
}
