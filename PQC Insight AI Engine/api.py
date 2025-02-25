from fastapi import FastAPI
from pydantic import BaseModel
from analyze_pqc import analyze_environment

app = FastAPI()

class EnvironmentInput(BaseModel):
    os_type: str
    crypto_lib: str
    web_server: str
    cert_type: str

@app.post("/analyze")
def analyze(input_data: EnvironmentInput):
    return analyze_environment(input_data.os_type, input_data.crypto_lib, input_data.web_server, input_data.cert_type)

# Run API: uvicorn api:app --reload

