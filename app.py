import streamlit as st
import requests

# ── PAGE CONFIG ──
st.set_page_config(
    page_title="AI Resume Builder",
    page_icon="📄",
    layout="centered"
)

# ── STYLES ──
st.markdown("""
<style>
    .block-container { max-width: 780px; padding-top: 2rem; }
    .title-block { text-align: center; padding: 0 0 1.5rem 0; }
    .title-block h1 { font-size: 2.2rem; font-weight: 800; margin-bottom: 0.3rem; }
    .title-block p  { color: #aaa; font-size: 1rem; margin: 0; }
    .step-label { font-weight: 700; font-size: 1rem; margin-bottom: 6px; }
    .drive-link-box {
        background: #1e2a1e;
        border: 1px solid #3a7a3a;
        border-radius: 10px;
        padding: 18px 22px;
        margin-top: 10px;
    }
    .drive-link-box a {
        font-size: 1.1rem;
        font-weight: 600;
        color: #5cdb5c;
        text-decoration: none;
    }
    .drive-link-box a:hover { text-decoration: underline; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-block">
    <h1>📄 AI Resume Builder</h1>
    <p>Paste a Job Description + your LaTeX template → get a tailored 1-page PDF on Google Drive</p>
</div>
""", unsafe_allow_html=True)

# ── DEFAULT LATEX TEMPLATE ──
DEFAULT_LATEX = r"""
\documentclass[10pt,a4paper]{article}
\usepackage[top=0.5in,bottom=0.4in,left=0.5in,right=0.5in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{hyperref}
\usepackage{enumitem}
\setlist{nolistsep, topsep=0pt, parsep=1pt, partopsep=0pt}
\usepackage{titlesec}
\titleformat{\section}{\bfseries\normalsize}{}{0em}{}[\titlerule]
\titlespacing{\section}{0pt}{4pt}{3pt}
\pagestyle{empty}

\begin{document}

% ── HEADER ──
\begin{center}
  {\Large\bfseries Sankalp Shukla} \\[2pt]
  {\small Remote / Work From Home \quad|\quad +91 8874745250 \quad|\quad
  \href{mailto:sankalpshukla212@gmail.com}{sankalpshukla212@gmail.com}} \\[1pt]
  {\small
  \href{https://sankalpshukla7474-creator.github.io/Sankalp_Portfolio/}{Portfolio} \quad|\quad
  \href{https://www.linkedin.com/in/sankalp-shukla-b77596316}{LinkedIn} \quad|\quad
  \href{https://github.com/sankalpshukla7474-creator}{GitHub} \quad|\quad
  \href{https://leetcode.com/u/Sankalp212/}{LeetCode} \quad|\quad
  \textbf{500+ DSA Solved}}
\end{center}

\section{Technical Skills}
\begin{itemize}
  \item \textbf{Programming \& Web:} Python (Advanced), JavaScript, React, HTML, CSS, REST APIs, FastAPI, Django, OOP
  \item \textbf{AI \& Generative AI:} LLMs, Transformers, Prompt Engineering, LangChain, LangGraph, Hugging Face, RAG Pipelines, NLP
  \item \textbf{ML \& MLOps:} TensorFlow, PyTorch, Scikit-learn, Autoencoder Models, Time-Series Analysis, Model Deployment, Explainability
  \item \textbf{Cloud \& Infra:} AWS (Certified), Azure, Docker, CI/CD, Git, PostgreSQL, Pinecone, ChromaDB, SageMaker, Kubernetes
  \item \textbf{Data \& Tools:} Signal Processing, Pandas, NumPy, Data Preprocessing, Structured Logging
\end{itemize}

\section{Experience}

\textbf{Freelance AI \& Software Engineer} \hfill \textit{May 2026 -- Present} \\
\textit{Independent Consultant --- Global / Remote}
\begin{itemize}
  \item Designed AI/ML apps integrating LLMs into production REST APIs using FastAPI; processed 20,000+ data points per pipeline, reducing overhead by 40\% and improving model accuracy by 15\%.
  \item Implemented RAG pipelines (LangChain, Hugging Face, Pinecone, ChromaDB); integrated OpenAI GPT \& Claude API into multi-agent automation workflows with prompt engineering.
\end{itemize}

\textbf{Junior AI Engineer Intern} \hfill \textit{Apr 2026 -- Oct 2026} \\
\textit{Globe Spring Solutions --- Ghaziabad, India}
\begin{itemize}
  \item Deployed GenAI tools and LLM-based apps for enterprise use; implemented transformer models with prompt optimization, reducing inference latency.
  \item Ensured ethical AI practices: bias mitigation, model explainability, and responsible deployment standards.
\end{itemize}

\textbf{Machine Learning Engineer Intern} \hfill \textit{Feb 2026 -- Apr 2026} \\
\textit{Globe Spring Solutions --- Ghaziabad, India}
\begin{itemize}
  \item Built Python/Pandas preprocessing pipelines for ML workflows, reducing manual overhead by 40\%; trained and evaluated deep learning models using TensorFlow.
\end{itemize}

\section{Key AI \& Software Engineering Projects}

\textbf{Industrial Anomaly Detection System} \hfill \href{https://github.com/sankalpshukla7474-creator}{[GitHub]} \\
\textit{Python, TensorFlow, Autoencoder, FastAPI, Docker, AWS}
\begin{itemize}
  \item Trained autoencoder on 20,000+ time-series telemetry points; full ML pipeline from preprocessing to Docker containerization and AWS deployment.
\end{itemize}

\textbf{Generative AI Document Intelligence Platform} \hfill \href{https://github.com/sankalpshukla7474-creator}{[GitHub]} \\
\textit{Python, LangChain, Hugging Face, Pinecone, FastAPI, React, Llama 3}
\begin{itemize}
  \item Full-stack GenAI app with React + FastAPI; custom 0--100\% hallucination trust-scoring engine with transformer embeddings and Pinecone vector storage.
\end{itemize}

\textbf{Multi-Agent AI Automation Platform} \hfill \href{https://github.com/sankalpshukla7474-creator}{[GitHub]} \\
\textit{Python, LangGraph, OpenAI GPT, FastAPI, PostgreSQL, Redis, Docker, Azure}
\begin{itemize}
  \item Architected multi-agent LLM system on Azure with LangGraph; REST APIs connecting agents to CRM and Google Sheets --- enabling 10+ hrs/week automation.
\end{itemize}

\section{Achievements}
\begin{itemize}
  \item \textbf{500+ DSA Solved} on LeetCode \quad|\quad \textbf{Best Innovation Award} --- Build With Gemini Hackathon, Delhi University (Team Lead) Nov 2025
  \item \textbf{1st Runner-Up} --- AI Global Summit 2K26, GLA University (Team Lead) Nov 2025 \quad|\quad \textbf{1st Runner-Up} --- Vibe Coding Hackathon, BMIET Sonipat Oct 2025
\end{itemize}

\section{Certifications \& Education}
\textbf{AWS Certified AI Practitioner (AIF-C01)} \& \textbf{AWS Cloud Practitioner (CLF-C02)} \hfill Feb 2026 \\
\textbf{KIET Group Of Institutions} (AKTU) --- B.Tech Computer Science Engineering \textbf{(80\%)} \hfill Current

\end{document}
""".strip()

# ── STEP 1: WEBHOOK URL ──
st.markdown('<div class="step-label">⚙️ Step 1: Your n8n Webhook URL</div>', unsafe_allow_html=True)
webhook_url = st.text_input(
    label="Webhook URL",
    placeholder="https://your-n8n-instance.com/webhook/xxxxxxxx",
    label_visibility="collapsed"
)
st.caption("Find this in your n8n Webhook node → 'Production URL'")

st.divider()

# ── STEP 2: JOB DESCRIPTION ──
st.markdown('<div class="step-label">📋 Step 2: Paste the Job Description</div>', unsafe_allow_html=True)
jd_input = st.text_area(
    label="Job Description",
    placeholder="Paste the full job description here...\n\nExample:\nWe are looking for a Senior ML Engineer with experience in LLMs, Python, FastAPI, RAG pipelines...",
    height=200,
    label_visibility="collapsed"
)

st.divider()

# ── STEP 3: LATEX CODE ──
st.markdown('<div class="step-label">🔧 Step 3: LaTeX Template (pre-filled — edit if needed)</div>', unsafe_allow_html=True)
latex_input = st.text_area(
    label="LaTeX Code",
    value=DEFAULT_LATEX,
    height=260,
    label_visibility="collapsed"
)
st.caption("This is your base resume in LaTeX. The AI will rewrite it to match the JD.")

st.divider()

# ── GENERATE ──
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_btn = st.button("✨ Generate Resume", use_container_width=True, type="primary")

# ── MAIN LOGIC ──
if generate_btn:
    if not webhook_url.strip():
        st.error("Please enter your n8n webhook URL.")
    elif not jd_input.strip():
        st.error("Please paste a job description.")
    elif not latex_input.strip():
        st.error("LaTeX code cannot be empty.")
    else:
        with st.spinner("🤖 Sending to your n8n workflow... this may take 20–40 seconds"):
            try:
                payload = {
                    "job_description": jd_input.strip(),
                    "latex_code": latex_input.strip()
                }
                response = requests.post(
                    webhook_url.strip(),
                    json=payload,
                    timeout=120
                )
                response.raise_for_status()

                # ── PARSE RESPONSE ──
                data = response.json()

                # Try common key names for the drive link
                drive_link = (
                    data.get("drive_link") or
                    data.get("google_drive_link") or
                    data.get("pdf_link") or
                    data.get("link") or
                    data.get("url") or
                    data.get("file_url") or
                    data.get("output") or
                    None
                )

                st.session_state["drive_link"] = drive_link
                st.session_state["raw_response"] = data

            except requests.exceptions.Timeout:
                st.error("⏱️ Request timed out (>120s). Check if your n8n workflow is running.")
            except requests.exceptions.ConnectionError:
                st.error("🔌 Could not connect to webhook. Make sure n8n is running and the URL is correct.")
            except requests.exceptions.HTTPError as e:
                st.error(f"❌ Webhook returned error: {e.response.status_code} — {e.response.text[:300]}")
            except Exception as e:
                st.error(f"Unexpected error: {e}")

# ── OUTPUT ──
if "drive_link" in st.session_state:
    st.divider()
    st.markdown('<div class="step-label">✅ Step 4: Your Resume is Ready!</div>', unsafe_allow_html=True)

    if st.session_state["drive_link"]:
        st.markdown(f"""
        <div class="drive-link-box">
            🎉 &nbsp; <a href="{st.session_state['drive_link']}" target="_blank">
                📂 Open Resume PDF on Google Drive
            </a>
            <br><br>
            <span style="color:#aaa; font-size:0.85rem;">
                Click the link above → File → Download to save your PDF.
            </span>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Drive link not found in expected keys — show raw response so user can identify key
        st.warning("⚠️ Resume generated but couldn't find the Google Drive link automatically.")
        st.markdown("**Raw response from your webhook** — find the link key and let me know:")
        st.json(st.session_state["raw_response"])

    # Reset button
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Generate Another", use_container_width=False):
        del st.session_state["drive_link"]
        del st.session_state["raw_response"]
        st.rerun()

# ── FOOTER ──
st.divider()
st.markdown(
    "<div style='text-align:center; color:#555; font-size:0.8rem;'>Built by Sankalp Shukla &nbsp;|&nbsp; Powered by n8n + AI</div>",
    unsafe_allow_html=True
)
