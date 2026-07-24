# 🧠 Mini RAG App

A lightweight **Retrieval-Augmented Generation (RAG)** application built to explore the fundamentals of modern LLM-powered systems. This project demonstrates how documents are processed, embedded, stored in a vector database, retrieved based on semantic similarity, and used to generate context-aware responses with a Large Language Model.

---

## 🚀 Features

- 📄 Document Loading
- ✂️ Text Chunking
- 🔎 Semantic Embeddings
- 🗂️ Vector Database Storage
- 🎯 Similarity Search
- 🤖 Retrieval-Augmented Generation (RAG)
- 💬 Context-Aware Question Answering

---

## 🛠️ Tech Stack

- Python
- LangChain
- Hugging Face
- ChromaDB / FAISS
- Sentence Transformers
- Ollama / OpenAI (depending on the selected LLM)

---

## 📁 Project Structure

```text
mini-rag-app/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
├── src/
└── notebooks/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone git@github.com:youssifshalaby/mini-rag-app.git
cd mini-rag-app
```

### Create a Conda environment

```bash
conda create -n mini-rag python=3.11
conda activate mini-rag
```
### (Optional) Setup you command line interface for better readability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN Collection

Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)
---

## 🎯 Learning Objectives

This project is built to understand the complete RAG pipeline, including:

- Loading documents
- Splitting text into chunks
- Creating embeddings
- Storing embeddings in a vector database
- Retrieving relevant information
- Generating responses with an LLM

---

## 📌 Future Improvements

- [ ] Support PDF, DOCX, and TXT documents
- [ ] Add conversational memory
- [ ] Build a Streamlit web interface
- [ ] Integrate local LLMs with Ollama
- [ ] Support multiple vector databases
- [ ] Deploy the application

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## 📄 License

This project is intended for educational purposes.