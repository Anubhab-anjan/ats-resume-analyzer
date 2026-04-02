from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from models import AnalyzeRequest, AnalyzeResponse
from ai_service import analyze_resume
from pdf_parser import extract_text_from_pdf

app = FastAPI(title="ATS Resume Analyzer", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "ATS Analyzer is running"}


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

    file_bytes = await file.read()

    if len(file_bytes) > 5 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="File too large. Max size is 5MB"
        )

    resume_text = extract_text_from_pdf(file_bytes)

    if not resume_text:
        raise HTTPException(
            status_code=422,
            detail="Could not extract text from PDF. Make sure it is not a scanned image."
        )

    return {
        "resume_text": resume_text,
        "char_count": len(resume_text),
        "word_count": len(resume_text.split())
    }


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest):
    if not req.resume_text.strip():
        raise HTTPException(status_code=400, detail="Resume text cannot be empty")

    if not req.job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty")

    if not req.company_name.strip():
        raise HTTPException(status_code=400, detail="Company name cannot be empty")

    if not req.role.strip():
        raise HTTPException(status_code=400, detail="Role cannot be empty")

    try:
        result = analyze_resume(
            resume_text=req.resume_text,
            job_description=req.job_description,
            company_name=req.company_name,
            role=req.role
        )
        return AnalyzeResponse(**result)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI analysis failed: {str(e)}"
        )


@app.get("/", response_class=HTMLResponse)
def serve_ui():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()
