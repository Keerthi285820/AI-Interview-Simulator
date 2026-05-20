# 🤖 AI Interview Simulator

An AI-powered interview practice platform built using Python, Streamlit, and NLP-based semantic evaluation.  
The system evaluates interview answers based on semantic similarity instead of simple keyword matching.

---

## 🚀 Features
- Topic-based interview selection
- Interactive question-answer interface
- NLP-based answer evaluation
- Semantic similarity scoring
- Instant feedback generation
- Streamlit web application

---

## 📚 Topics Included
- Machine Learning
- Python
- SQL

---

## 🛠️ Tech Stack
- Python
- Streamlit
- Sentence Transformers
- Scikit-learn

---

## 📂 Project Structure

```text
ai-interview-simulator/
│
├── app.py
├── questions.py
├── evaluator.py
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

```text
User Answer
    ↓
Sentence Embedding
    ↓
Expected Answer Embedding
    ↓
Cosine Similarity
    ↓
Score + Feedback
```

The system compares the meaning of the user's answer with the expected answer using NLP-based semantic similarity.

---

## ▶️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🚀 Future Enhancements
- AI-generated interview questions
- Resume-based interviews
- Voice interview support
- LLM integration
- Performance analytics dashboard

---

## 📌 Project Status
✅ Level 1 Completed  
✅ Level 2 Completed  
🚀 More advanced AI features coming soon

---

## 👨‍💻 Author
Built as part of my AI/ML learning journey while exploring practical and real-world AI systems.
