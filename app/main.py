'''
Hare Krishna, Hare Krishna Krishna Krishna Hare Hare, Hare Rama Hare Rama Rama Rama Hare Hare
Best Wishes from Shelly And Aayush
'''

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# Define a model for text input
class TextInput(BaseModel):
  text: Optional[str] = None  # Text Input is Optional


@app.post("/process-input/")
async def process_input(input: Optional[TextInput] = None,
                        file: Optional[UploadFile] = File(None)):

  # Case 1: No Input Provided:
  if not input or not input.text and not file:
    raise HTTPException(
        status_code=400,
        detail="Please provide either text input, a file, or both.")

  result = {}
  # Case 2: Process text input if provided
  if input and input.text:
    result["text"] = f"Processed text: {input.text}"

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
