# KTU Desktop RAG (Retrieval-Augmented Generation)

**KTU Desktop RAG** is a desktop application built to assist students of **Kerala Technological University (KTU)** in accessing accurate information from textbooks, notes, and other academic resources. The project leverages **Ollama**'s advanced RAG model to provide precise answers to student queries by integrating retrieval and generative AI capabilities. Designed with a user-friendly GUI using **Tkinter**, the tool aims to simplify academic search and enhance the learning experience.

---

## Features (Planned and Ongoing)
- **Document Upload**:
  - Allows users to upload academic resources like textbooks, notes, PDFs, and other course materials.
- **Semantic Search**:
  - Employs Ollama's RAG model to retrieve the most relevant text chunks from the uploaded documents.
- **Conversational AI**:
  - Provides accurate and contextual answers to user queries by combining retrieval and generative AI.
- **Desktop GUI**:
  - Built using Tkinter to offer a simple, responsive, and intuitive interface.
- **Multi-Document Support** (Planned):
  - Support for managing and querying across multiple academic documents simultaneously.
- **Offline Functionality** (Planned):
  - Aiming to provide partial offline support for semantic search while maintaining generative capabilities online.

---

## Technologies Used
- **Ollama RAG Model**:
  - Powers the backend with its robust Retrieval-Augmented Generation (RAG) capabilities.
- **Tkinter**:
  - Framework for building the desktop GUI.
- **Python**:
  - Core programming language for the application.
- **FAISS** (Planned):
  - For vector-based semantic search to efficiently retrieve relevant document segments.
- **SQLite** (Planned):
  - Lightweight database to manage metadata and indexing of uploaded documents.

---

## Installation (Work in Progress)

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd ktu-desktop-rag
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

   *(This step is subject to change as the project evolves.)*

---

## Usage (Planned Workflow)
1. **Launch the application**:
   - Start the app from the desktop shortcut or via `python main.py`.
2. **Upload Academic Resources**:
   - Add textbooks, notes, or PDFs via the upload feature.
3. **Ask Questions**:
   - Enter a query in the provided input box. Example: *"What are the applications of Machine Learning in engineering?"*
4. **Receive Accurate Answers**:
   - The system will retrieve the most relevant sections from the uploaded documents and generate an accurate response using the Ollama RAG model.

---

## Contribution

This project is currently under development. Contributions are welcome as we aim to build a robust tool for KTU students.

### How to Contribute
1. Fork the repository and create a new branch.
2. Work on the feature or fix you wish to contribute.
3. Submit a pull request with a clear description of your changes.

---

## Roadmap

- [ ] Implement multi-document support.
- [ ] Integrate FAISS for efficient text chunk indexing and retrieval.
- [ ] Improve the Tkinter GUI with better responsiveness and modern design.
- [ ] Enable offline functionality for semantic search.
- [ ] Add support for course-specific resources and tagging.

---

## Acknowledgments

- **Ollama**: For providing the RAG model that powers the backend.
- **Tkinter**: For simplifying desktop GUI development.
- **Kerala Technological University**: The academic community inspiring the creation of this tool.

---

## Disclaimer

This project is a work in progress and is being developed specifically for educational purposes. It is not officially affiliated with Kerala Technological University (KTU).

---
