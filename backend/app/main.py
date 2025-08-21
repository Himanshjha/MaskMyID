from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
import uuid
import os

from app.ocr import extract_text
from app.detection import detect_pii
from app.masking import mask_pii

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "MaskMyID backend is running ✅"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # Save uploaded file
    file_ext = file.filename.split(".")[-1]
    file_name = f"{uuid.uuid4()}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, file_name)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text + bounding boxes
    ocr_results, image = extract_text(file_path)

    # Detect PII
    pii_boxes = detect_pii(ocr_results)

    # Mask image
    output_path = os.path.join(OUTPUT_DIR, file_name)
    masked_image = mask_pii(image, pii_boxes)
    masked_image.save(output_path)

    return FileResponse(output_path, media_type="image/png")
