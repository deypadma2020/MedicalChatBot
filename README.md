# MedicalChatBot

# 🩺 Medical ChatBot

An AI-powered Medical ChatBot built using Retrieval-Augmented Generation (RAG) architecture.  
The chatbot answers medical-related queries using custom PDF documents as the knowledge base.

The project uses FAISS as the vector database, HuggingFace embeddings for semantic search, and Groq LLM for fast AI-generated responses.

🌐 Live Demo: https://medicalchatbot-lu0d.onrender.com

---

# 🚀 Features

- AI-powered Medical Question Answering
- Retrieval-Augmented Generation (RAG)
- PDF document-based knowledge retrieval
- Semantic Search using FAISS
- Fast inference using Groq LLM
- HuggingFace Embedding Model integration
- Streamlit interactive UI
- Modular and scalable architecture
- Local vector database storage
- Render deployment support

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend
- Python
- LangChain

## Vector Database
- FAISS

## Embedding Model
- sentence-transformers/all-MiniLM-L6-v2

## Large Language Model (LLM)
- Groq API
- Llama 3.3 70B Versatile

## Document Processing
- PyPDFLoader
- RecursiveCharacterTextSplitter

## Deployment
- Render

---

# 📂 Project Structure

```bash
MedicalChatBot/
│
├── data/                         # PDF files
│
├── faiss_index/                  # Saved FAISS vector database
│   ├── index.faiss
│   └── index.pkl
│
├── research/
│   └── trials.ipynb
│
├── src/
│   ├── __init__.py
│   ├── helper.py                 # Helper functions
│   ├── prompt.py                 # System prompt
│   └── rag_chain.py              # RAG chain creation
│
├── app.py                        # Terminal chatbot app
├── streamlit_app.py              # Streamlit UI app
├── store_index.py                # Create FAISS vector database
│
├── requirements.txt
├── setup.py
├── render.yaml
├── .env
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/deypadma2020/MedicalChatBot.git

cd MedicalChatBot
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv medbot_venv
```

Activate Environment:

```bash
medbot_venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# 📄 Add PDF Documents

Place all your medical PDF files inside:

```bash
data/
```

---

# 🧠 Create FAISS Vector Database

Run the following command:

```bash
python store_index.py
```

This will generate:

```bash
faiss_index/
```

containing:

- `index.faiss`
- `index.pkl`

---

# ▶️ Run the Application

## Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

## Terminal Chatbot

```bash
python app.py
```

---

# 🌐 Deployment on Render

## Build Command

```bash
pip install -r requirements.txt
```

## Start Command

```bash
streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0
```

## Environment Variables

```env
PYTHON_VERSION=3.10.11
GROQ_API_KEY=your_groq_api_key
```

---

# 🧩 How It Works

1. Load PDF documents
2. Split documents into smaller chunks
3. Generate embeddings using HuggingFace model
4. Store embeddings in FAISS vector database
5. Retrieve relevant chunks using semantic similarity
6. Send retrieved context to LLM
7. Generate accurate AI response

---

# 📌 Future Improvements

- Chat history memory
- Multi-user authentication
- Streaming responses
- Cloud vector database support
- Conversation summarization
- Docker containerization
- Medical source citation support

---

# ⚠️ Disclaimer

This chatbot is for educational and informational purposes only.  
It should not be considered professional medical advice, diagnosis, or treatment.

---

# 👨‍💻 Author

Padma Dey

GitHub: https://github.com/deypadma2020

Project Repository:
https://github.com/deypadma2020/MedicalChatBot

Live Demo:
https://medicalchatbot-lu0d.onrender.com