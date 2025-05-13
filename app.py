from flask import Flask, render_template, request, jsonify
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os
import re
import sqlite3
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

# Load environment variables
os.environ["GROQ_API_KEY"] = ""
# Initialize SQLite database for feedback
def init_db():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS feedback
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  query TEXT,
                  answer TEXT,
                  rating TEXT,
                  comment TEXT,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

init_db()

loader = PyPDFLoader('INHERITANCE-IN-ISLAM.pdf')  # Replace with your PDF file path
documents = loader.load()

    # Split the text into chunks
text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
docs = text_splitter.split_documents(documents)
# Initialize RAG components
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
chroma_db = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory='./chroma_db'
    )

llm = ChatGroq(
    model="llama-3.1-8b-instant",  # You can choose a different model if needed
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,)

retriever = chroma_db.as_retriever(search_kwargs={"k": 3})









qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    try:
        user_query = request.form.get('query')
        if not user_query:
            return jsonify({'error': 'Query cannot be empty'}), 400
        result = qa_chain.run(user_query)
        return jsonify({'answer': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        data = request.form
        query = data.get('query')
        answer = data.get('answer')
        rating = data.get('rating')
        comment = data.get('comment', '')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()
        c.execute('''INSERT INTO feedback (query, answer, rating, comment, timestamp)
                     VALUES (?, ?, ?, ?, ?)''', (query, answer, rating, comment, timestamp))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Feedback submitted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)