from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from typing import Optional

app = FastAPI()


@app.post("/process-input/")
async def process_input(
    text: Optional[str] = Form(None),  # Accept text as form-data
    file: Optional[UploadFile] = File(None)  # Accept file input
):
  # Case 1: No Input Provided
  if not text and not file:
    raise HTTPException(
        status_code=400,
        detail="Please provide either text input, a file, or both.")

  result = {}

  # Case 2: Process text input if provided
  if text:
    result["text"] = f"Processed text: {text}"

  # Case 3: Process file input if provided
  if file:
    content = await file.read()
    result["file"] = {
        "filename": file.filename,
        "content_preview":
        content.decode('utf-8')[:100]  # Preview first 100 characters
    }

  return {
      "status": "success",
      "data": result,
      "message": "Input processed successfully"
  }
