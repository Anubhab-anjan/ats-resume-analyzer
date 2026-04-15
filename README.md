# 🧬 ResumeX — AI-Powered ATS Resume Analyzer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

**Decode what ATS systems really look for — analyze your resume against any job description with AI.**

</div>

---

## ✨ Features

- **📄 PDF Resume Parsing** — Upload your resume as a PDF and extract text automatically
- **🤖 AI-Powered Analysis** — Uses Meta's Llama 3.3 70B model via Hugging Face for intelligent scoring
- **📊 ATS Compatibility Score** — Get an overall score (0–100) for how well your resume matches the job
- **🔍 Keyword Matching** — See which keywords you hit and which ones you're missing
- **💡 Actionable Suggestions** — Receive prioritized improvement tips tailored to the company and role
- **🎨 Stunning UI** — Sci-fi inspired glassmorphism interface with particle animations and radial gauges

## 📸 Screenshots

### Upload Step
The drag-and-drop upload interface with word/character stats.

### Analysis Dashboard
Animated radial score gauge, sub-score cards, keyword chips, and prioritized suggestions.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- A free [Hugging Face](https://huggingface.co/) account & API token

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/ats-resume-analyzer.git
cd ats-resume-analyzer
```

### 2. Create a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Edit `.env` and add your Hugging Face API key:

```
HUGGINGFACE_API_KEY=hf_your_token_here
```

> 🔑 Get your free token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### 5. Run the app

```bash
uvicorn main:app --reload --port 8000
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🏗️ How It Works

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐     ┌──────────────┐
│  Upload PDF │────▶│  Extract Text│────▶│  Send to Llama   │────▶│  Display     │
│  (Frontend) │     │  (pdfplumber)│     │  3.3 via HF API  │     │  Results     │
└─────────────┘     └──────────────┘     └─────────────────┘     └──────────────┘
```

1. **Upload** — User drops a PDF resume into the browser
2. **Parse** — `pdfplumber` extracts raw text from the PDF
3. **Analyze** — The text + job description are sent to Llama 3.3 70B, which returns structured JSON with scores, keywords, and suggestions
4. **Visualize** — The frontend renders animated gauges, keyword chips, and prioritized suggestion cards

---

## 📁 Project Structure

```
├── main.py              # FastAPI routes & server
├── ai_service.py        # Hugging Face AI integration
├── models.py            # Pydantic request/response schemas
├── pdf_parser.py         # PDF text extraction
├── index.html           # Frontend UI (single-file)
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
└── .gitignore           # Git exclusions
```

---

## 🛠️ API Endpoints

| Method | Endpoint          | Description                          |
|--------|-------------------|--------------------------------------|
| `GET`  | `/`               | Serves the frontend UI               |
| `GET`  | `/health`         | Health check                         |
| `POST` | `/upload-resume`  | Upload a PDF and extract text        |
| `POST` | `/analyze`        | Analyze resume against job description |

---

## 🧠 Tech Stack

- **Backend:** FastAPI + Uvicorn
- **AI Model:** Meta Llama 3.3 70B Instruct (via Hugging Face Inference API)
- **PDF Parsing:** pdfplumber
- **Frontend:** Vanilla HTML/CSS/JS with canvas particle engine & glassmorphism design

----

## 📄 License

MIT — free to use, modify, and distribute.

---

<div align="center">
  <b>Built with ❤️ by Anubh</b>
</div>
