from fastapi import FastAPI
import json
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

with open("q-vercel-python.json", "r") as file:
    students_data = json.load(file)

@app.get("/api")
def read_api(x: Optional[str] = None, y: Optional[str] = None):
    # Default to 0 if parameter is not provided or not found
    xMarks = next((student["marks"] for student in students_data if student["name"] == x), 0)
    yMarks = next((student["marks"] for student in students_data if student["name"] == y), 0)
    
    return {"marks": [xMarks, yMarks]}
    
@app.get("/")
def read_api(x: Optional[str] = None, y: Optional[str] = None):
    # Default to 0 if parameter is not provided or not found
    xMarks = next((student["marks"] for student in students_data if student["name"] == x), 0)
    yMarks = next((student["marks"] for student in students_data if student["name"] == y), 0)
    
    return {"marks": [ xMarks, yMarks]}