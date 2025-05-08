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

@app.get("/")
def read_root():
    return {
        "message": "Hello World"
    }

@app.get("/api")
def read_root(x: Optional[str] = None, y: Optional[str] = None):
    xMarks = next((student["marks"] for student in students_data if student["name"] == x), None)
    yMarks = next((student["marks"] for student in students_data if student["name"] == y), None)
    
    return {
        "marks": [
            xMarks, yMarks
        ]
    }