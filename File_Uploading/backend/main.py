from fastapi import FastAPI, UploadFile, File,HTTPException,status
from fastapi.staticfiles import StaticFiles
import os
import fitz
import shutil
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

UPLOADS_DIR = "uploads"
os.makedirs(UPLOADS_DIR, exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_text_from_document(document):
    doc = fitz.open(document)
    text = ''
    for page in doc:
        text+=page.get_text()
    doc.close()
    return text

@app.get("/")
def home():
    return {"message": "FastAPI File Upload API"}

    
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Only PDF files are allowed."
        )

    file_path = os.path.join(UPLOADS_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_document(file_path)

    return {
        "filename": file.filename,
        "text": text
    }