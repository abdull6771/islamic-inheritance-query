
````markdown
Islamic Inheritance Query

A Flask-based web application that allows users to query Islamic inheritance laws using a Retrieval-Augmented Generation (RAG) system powered by LangChain, ChromaDB, and OpenAI's `gpt-4o-mini` model. The application features an Islamic-themed interface with Quranic verses, query history, feedback collection, and accessibility considerations.



 🌟 Features

- Query Interface: Ask questions about Islamic inheritance laws (e.g., _"How is the estate distributed if a man leaves a wife and two daughters?"_).
- RAG Pipeline: Retrieves relevant information from a pre-indexed PDF using ChromaDB and generates answers with OpenAI’s `gpt-4o-mini`.
- Query History: Stores up to 5 recent queries in the browser's `localStorage` with a "Clear History" button.
- Feedback Mechanism: Users can rate answers (thumbs-up/down) or provide comments, stored in a SQLite database.
- Quranic Verses: Displays relevant verses from Surah An-Nisa (4:11, 4:12, 4:176) with Arabic text, transliteration, and English translation.
- Islamic Design: Tailwind CSS with a green and gold color scheme, Amiri font for Arabic text, and Islamic imagery.
- Accessibility: ARIA attributes and responsive design for better usability.


🛠 Tech Stack

- Backend: Flask (Python), LangChain, ChromaDB, OpenAI API (`gpt-4o-mini`)
- Frontend: HTML, Tailwind CSS, jQuery
- Database: SQLite (for feedback storage)
- Embedding Model: SentenceTransformer (`all-MiniLM-L6-v2`)
- Fonts: Amiri (for Arabic text)



⚙️ Prerequisites

- Python 3.8+
- Git
- OpenAI API Key ([Get one here](https://platform.openai.com/signup))
- A pre-indexed ChromaDB directory (`chroma_db`) generated from a Jupyter notebook processing an Islamic inheritance PDF


🚀 Installation

1. Clone the Repository

```bash
git clone https://github.com/abdull6771/islamic-inheritance-query.git
cd islamic-inheritance-query
````

2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Dependencies

```bash
pip install flask langchain chromadb sentence-transformers openai python-dotenv
```

4. Configure Environment Variables

Create a `.env` file in the project root:

```ini
OPENAI_API_KEY=your_openai_api_key
```

5. Ensure ChromaDB Directory

Place the `chroma_db` directory (generated from a Jupyter notebook) in the project root. This contains the vectorized Islamic inheritance PDF data.

---

🧪 Usage

Run the Application

```bash
python app.py
```

Access the Web Interface

Open your browser and go to:

```
http://127.0.0.1:5000
```

Query Examples

* *"Who are the male heirs in Islamic inheritance?"*
* *"What is the share of a daughter if there are no sons?"*

Use the query form, view answers, and provide feedback via thumbs-up/down or comments.

Manage Query History

* View recent queries in the sidebar (visible on large screens).
* Click **Clear History** to remove all stored queries.

---

## 📁 Project Structure

```
islamic-inheritance-query/
├── app.py                  # Flask application with RAG pipeline and routes
├── templates/
│   └── index.html          # Frontend with query form, Quranic verses, and feedback
├── chroma_db/              # ChromaDB directory with vectorized PDF data
├── feedback.db             # SQLite database for feedback (created automatically)
├── .env                    # Environment variables (not tracked)
└── README.md               # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:

   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

Please ensure code follows **PEP 8** (Python) and **W3C standards** (HTML/CSS). Add tests for new features and update documentation as needed.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

* Thanks to **Unsplash** for Islamic-themed images.
* Powered by **LangChain**, **ChromaDB**, and **OpenAI**.

```

```
