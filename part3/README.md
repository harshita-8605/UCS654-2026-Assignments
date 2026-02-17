TOPSIS Web Service (FastAPI)

This project implements TOPSIS as a web service using FastAPI.

The user uploads:
- CSV file
- Weights
- Impacts
- Email ID

The service computes TOPSIS score and returns the result file.

Run instructions:
pip install -r requirements.txt
uvicorn app:app --reload

Open:
http://127.0.0.1:8000/docs
