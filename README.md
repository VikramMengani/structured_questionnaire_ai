# 📘 Structured Questionnaire Answering Tool  
AI-Powered Vendor & Compliance Questionnaire Automation System  

---

## 🚀 Overview

This project is an end-to-end AI-powered Structured Questionnaire Answering Tool designed to automate vendor security and compliance questionnaires using grounded reference documentation.

The system enables users to:

- Authenticate securely  
- Upload structured questionnaires  
- Retrieve answers from internal reference documents  
- Generate citation-backed responses  
- Review and edit answers  
- Export structured documents in original format  

The solution demonstrates applied AI engineering, retrieval-based reasoning, persistent storage, and workflow design.

---

## 🏢 Industry & Fictional Company

### Industry  
Cybersecurity SaaS  

### Fictional Company  
SecureLayer AI  

SecureLayer AI is a B2B SaaS cybersecurity platform that provides automated compliance monitoring and security posture management. The company helps organizations maintain SOC 2 and ISO 27001 compliance through continuous monitoring, encryption controls, and audit automation.

---

## 🎯 Problem Statement

Security and compliance teams frequently receive structured questionnaires (SOC 2, vendor risk assessments, operational audits). These must be answered using approved internal documentation.

Manual answering is:

- Time-consuming  
- Error-prone  
- Inconsistent  
- Difficult to track  

This system automates that workflow using grounded AI retrieval.

---

## 🛠 What I Built

An end-to-end system that includes:

- 🔐 User Authentication (Signup/Login)  
- 🗄 PostgreSQL persistent database  
- 📄 Questionnaire upload & parsing  
- 📚 Reference document indexing  
- 🧠 Vector-based retrieval (TF-IDF + FAISS)  
- 📌 Citation-backed answer generation  
- 📊 Confidence scoring  
- ✏ Review & edit workflow  
- 📤 Structured DOCX export  
- 📈 Coverage summary  

---

## 🧠 System Architecture
User
  ↓
Login / Signup
  ↓
Upload Questionnaire
  ↓
Store Questions in Database
  ↓
Load Reference Documents
  ↓
Vectorize (TF-IDF)
  ↓
Index using FAISS
  ↓
Retrieve Most Relevant Chunk
  ↓
Extract Best Sentence
  ↓
Store Answer + Citation + Confidence
  ↓
Review & Edit
  ↓
Export Structured DOCX


---

## 🧩 Core Workflow

### Phase 1 — Core Answering

- User uploads questionnaire (each line = one question)  
- System parses and stores questions  
- Reference documents are indexed  

For each question:

- Vector similarity search performed  
- Best matching chunk retrieved  
- Most relevant sentence extracted  
- Citation attached  
- Confidence score assigned  
- Answer stored in database  

If no relevant match is found:


Not found in references.


---

### Phase 2 — Review & Export

After generation:

- Users can retrieve all answers  
- Edit specific answers  
- Export structured DOCX document  
- View coverage summary  

Export preserves:

- Original question order  
- Unmodified question text  
- Answer below each question  
- Citation  
- Confidence score  

---

## 📊 Confidence Scoring Logic

Confidence is based on vector similarity distance:

- High → Strong semantic match  
- Medium → Moderate similarity  
- Low → Weak match  
- Not Found → No reliable reference  

This ensures outputs are grounded and explainable.

---

## 🗄 Database Design

Tables:

- Users  
- Questionnaires  
- Questions  
- Answers  

Relationships:


User → Questionnaire → Questions → Answers


Persistent storage ensures repeatability and structured data management.

---

## 🛠 Tech Stack

### Backend
- FastAPI  
- SQLAlchemy  
- PostgreSQL  
- FAISS  
- Scikit-learn (TF-IDF)  
- Python-docx  

### AI Logic
- Retrieval-based Question Answering  
- Vector similarity search  
- Sentence-level extraction  
- Citation grounding  

---

## 📂 Project Structure


structured-questionnaire-ai/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── auth.py
│   ├── rag.py
│
├── references/
├── uploads/
├── exports/
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚖ Assumptions

- Each line in questionnaire represents one question  
- Reference documents are authoritative source of truth  
- Questions are independent  
- System runs in single-user mode (no RBAC)  

---

## ⚖ Trade-offs Made

- Used TF-IDF instead of transformer embeddings to ensure:
  - Offline capability  
  - Faster deployment  
  - Lower computational cost  

- Sentence-level extraction instead of generative LLM to:
  - Avoid hallucinations  
  - Ensure grounded answers  

- Basic authentication instead of OAuth/JWT refresh flows  
- No advanced PDF parsing (text-based format used)  

---

## 🚀 Improvements With More Time

- Replace TF-IDF with transformer embeddings  
- Add partial regeneration per question  
- Add version history  
- Add UI frontend  
- Add highlighted evidence snippets  
- Add async background processing  
- Add multi-tenant user isolation  

---

## 📈 Coverage Summary Feature

The system provides:

- Total number of questions  
- Questions answered with citation  
- Questions marked “Not found in references”  

This gives visibility into documentation gaps.

---

## 🧪 How To Run Locally

### 1️⃣ Clone Repository


git clone <repo-link>
cd structured-questionnaire-ai


### 2️⃣ Create Virtual Environment


python -m venv venv
venv\Scripts\activate


### 3️⃣ Install Dependencies


pip install -r requirements.txt


### 4️⃣ Setup PostgreSQL

Create database:


CREATE DATABASE questionnaire_db;


### 5️⃣ Add Environment Variables


DATABASE_URL=postgresql://postgres:password@localhost:5432/questionnaire_db
SECRET_KEY=your_secret_key


### 6️⃣ Run Server


uvicorn app.main:app --reload


Open:


http://127.0.0.1:8000/docs


---

## 🎯 Why This Project Demonstrates GTM Engineering Skills

This project demonstrates:

- Applied AI engineering  
- Retrieval-based reasoning  
- Workflow orchestration  
- Database modeling  
- API architecture  
- Grounded output design  
- Trade-off decision making  
- End-to-end system thinking  

It prioritizes reliability and explainability over generative hallucination.

---

## 📌 Final Deliverables

- GitHub repository  
- Functional application  
- Persistent database  
- Citation-grounded answers  
- Structured export capability  
- Clear README documentation  

---

## 🧠 Summary

This project solves a real operational problem by combining:

- Structured parsing  
- Vector retrieval  
- Grounded answer extraction  
- Editable workflow  
- Structured export  

It demonstrates practical AI system design suitable for real-world enterprise use cases.

---

## 👨‍💻 Author

**Vikram Mengani**  
AI Engineer | Full Stack Developer | Machine Learning Enthusiast  

Vikram is an MCA graduate with hands-on experience in AI systems, vector search, and full-stack development. Passionate about building practical AI solutions that solve real-world operational problems.

🔗 LinkedIn: https://www.linkedin.com/in/vikram-mengani/  
💻 GitHub: https://github.com/VikramMengani  

---
