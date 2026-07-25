# ⚽ FIFA World Cup 2026 RAG Chatbot

An interactive, Retrieval-Augmented Generation (RAG) web application that provides accurate, real-time answers about the **2026 FIFA World Cup**. 

By combining **ChromaDB vector search** with **Groq's LLaMA 3.3 70B model**, the chatbot retrieves relevant tournament facts and uses them to ground its responses[cite: 8, 9].

---

## ✨ Features

* **Vector Search Retrieval:** Uses **ChromaDB** to persistently store and query domain-specific documents based on semantic similarity.
* **Context-Aware Generation:** Injects retrieved document context directly into system prompts before sending messages to the LLM.
* **Ultra-Fast LLM Execution:** Powered by Groq's high-speed `llama-3.3-70b-versatile` model.
* **Flask Web Dashboard:** Offers a simple backend interface and REST API (`/chat`) that accepts conversation streams and returns structured replies[cite: 8].
* **Custom Knowledge Base:** Comes pre-indexed with detailed facts regarding the 2026 FIFA World Cup host nations, team counts, semifinal results, and final schedules[cite: 9].

---

## 🛠️ Tech Stack

* **Backend Framework:** Flask `3.0.3`[cite: 8, 10]
* **LLM Provider:** Groq SDK `0.9.0` (`llama-3.3-70b-versatile`)[cite: 8, 10]
* **Vector Database:** ChromaDB Persistent Client[cite: 9]
* **Language:** Python[cite: 8, 9]

---

## 📁 Repository Structure

```text
.
├── app.py              # Flask server and RAG chat API endpoint[cite: 8]
├── rag_storage.py      # ChromaDB setup, indexing, and document retriever[cite: 9]
├── requirements.txt    # Dependencies (Flask & Groq)[cite: 10]
├── templates/
│   └── index.html      # Web interface template[cite: 8]
└── chroma_db/          # Persistent local vector database folder[cite: 9]
