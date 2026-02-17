from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import shutil
from topsis_logic import topsis

app = FastAPI()
@app.get("/")
def home():
    return {"message": "TOPSIS FastAPI service is running"}
    
@app.post("/topsis")
async def run_topsis(
    file: UploadFile = File(...),
    weights: str = Form(...),
    impacts: str = Form(...),
    email: str = Form(...)
):
    input_path = "input.csv"
    output_path = "result.csv"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    topsis(input_path, weights, impacts, output_path)

    return FileResponse(
        output_path,
        media_type="text/csv",
        filename="result.csv"
    )
