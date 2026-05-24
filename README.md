# 🚀 AI Resume Builder — n8n + Streamlit

An AI-powered Resume Builder that tailors LaTeX resumes according to a Job Description using LLMs, automatically generates a PDF, uploads it to Google Drive, and returns a shareable link.

---

## ✨ Features

- 📄 Paste any Job Description
- 🤖 AI rewrites resumes according to the JD
- 🧠 OpenRouter LLM integration
- 📝 Editable LaTeX resume template
- 📑 Automatic PDF generation
- ☁️ Google Drive upload automation
- 🔗 Public shareable PDF link
- 🌐 Streamlit frontend deployment
- ⚡ n8n workflow orchestration

---

# 🌐 Live Demo

🔗 [AI Resume Builder App](https://resumebuilder-yztfk3okq39bquhxw4foct.streamlit.app)

---

# 📂 GitHub Repository

🔗 [GitHub Repository](https://github.com/sankalpshukla7474-creator/resume_builder)

---

# 🏗️ System Architecture

```text
User Input (JD + Resume)
        ↓
Streamlit Frontend
        ↓
n8n Webhook
        ↓
OpenRouter LLM API
        ↓
LaTeX Resume Generation
        ↓
PDFShift PDF Conversion
        ↓
Google Drive Upload
        ↓
Public PDF Link Returned
```

---

# ⚙️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend logic |
| Streamlit | Frontend UI |
| n8n | Workflow automation |
| OpenRouter API | LLM integration |
| LaTeX | Resume formatting |
| PDFShift API | PDF generation |
| Google Drive API | File storage |
| ngrok | Public webhook tunneling |

---

# 📸 Screenshots

## 🔹 Streamlit Frontend

<img width="1919" height="973" alt="Frontend UI" src="https://github.com/user-attachments/assets/fa7c56bb-c34b-41be-b57c-fffef460d88d" />

---

## 🔹 n8n Workflow Automation

<img width="1919" height="987" alt="n8n Workflow" src="https://github.com/user-attachments/assets/05ddaea8-802b-4692-bcf9-7d2e509e32f7" />

---

# 🔥 Workflow Overview

The automation pipeline performs:

1. Receives Job Description from Streamlit
2. Sends prompt to OpenRouter LLM
3. Generates optimized LaTeX resume
4. Converts LaTeX → PDF
5. Uploads PDF to Google Drive
6. Returns public PDF link to frontend

---

# 🚀 Local Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sankalpshukla7474-creator/resume_builder.git
cd resume_builder
```

## 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

## 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 🔗 n8n Setup

## 1️⃣ Import the n8n Workflow JSON

Import your workflow into n8n.

## 2️⃣ Configure Required APIs

Add credentials for:

- OpenRouter API
- Google Drive API
- PDFShift API

## 3️⃣ Start n8n Locally

```bash
n8n start
```

## 4️⃣ Expose Localhost using ngrok

```bash
ngrok http 5678
```

## 5️⃣ Use Webhook URL

Example:

```text
https://your-ngrok-url/webhook/resume-generator
```

Paste this URL into the Streamlit application.

---

# 📦 Example Use Case

## ✅ Input

- Job Description for an ML Engineer role
- Base LaTeX resume template

## ✅ Output

- AI-tailored ATS-friendly PDF resume
- Public Google Drive link

---

# 🎥 Demo Video

🔗 [LinkedIn Demo](https://www.linkedin.com/in/sankalp212/)

---

# 💡 Future Improvements

- Multi-template support
- Resume scoring system
- ATS compatibility analyzer
- LinkedIn profile import
- Direct PDF download
- Authentication system
- Permanent n8n cloud deployment

---

# 👨‍💻 Author

## Sankalp Shukla

- 🔗 [GitHub](https://github.com/sankalpshukla7474-creator)
- 🔗 [LinkedIn](https://www.linkedin.com/in/sankalp212/)

---

# ⭐ Support

If you liked this project:

- ⭐ Star the repository
- 💬 Share feedback
- 🤝 Connect on LinkedIn

---

# 📜 License

This project is licensed under the MIT License.
