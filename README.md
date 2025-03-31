## 📚 Gutenberg Book Analyzer

A full-stack web application that fetches public domain books from [Project Gutenberg](https://www.gutenberg.org), analyzes them using an LLM (like OpenAI or Groq), identifies characters and their interactions, and visualizes the relationships in a dynamic graph.

---

### ✨ Features

- Input a **Project Gutenberg Book ID**
- Download book text automatically
- Use an **LLM to extract characters and interactions**
- Visualize interactions using a force-directed graph
- Display raw analysis result (JSON)
- Clean, no-Tailwind frontend with plain CSS
- Backend built with FastAPI
- Frontend built with React + Vite
- Dockerized deployment support

---

### 🧱 Tech Stack

| Layer     | Tech         |
|-----------|--------------|
| Frontend  | React (Vite) |
| Backend   | FastAPI      |
| LLM       | OpenAI / Groq / SambaNova |
| Graph     | react-force-graph |
| Deploy    | Docker / Docker Compose |

---

### 📦 Project Structure

```
gutenberg-analyzer/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       └── analysis.py
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/
│       ├── App.tsx
│       ├── components/
│       └── index.css
├── docker-compose.yml
└── README.md
```

---

### 🛠️ Getting Started

#### 1. Clone the repo

```bash
git clone https://github.com/yourusername/gutenberg-analyzer.git
cd gutenberg-analyzer
```

#### 2. Set up environment variable

You’ll need an LLM API key:

```bash
export OPENAI_API_KEY=your-openai-or-groq-key
```

> Or use `.env` with Docker

---

### 🐳 Run with Docker Compose

```bash
docker-compose up --build
```

- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend API: [http://localhost:8000/analyze/1787](http://localhost:8000/analyze/1787)

---

### 🔍 Example Book ID

> Federalist Papers: `1787`  
> Romeo and Juliet: `1513`

---

### 🖼️ Screenshots

**Input & Graph View**

![image](https://github.com/user-attachments/assets/7cbd1abe-7f50-49a6-87b9-83b0d7e8c946)


---

### 🧪 Development Scripts

**Frontend (React):**

```bash
cd frontend
npm install
npm run dev
```

**Backend (FastAPI):**

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

---

### ✅ To Do / Bonus Ideas

- [ ] Add quote/sentiment tagging
- [ ] Export analysis result as JSON
- [ ] Add search to filter characters
- [ ] Deploy to Vercel / Fly.io


### 📄 License
MIT
