from fastapi import FastAPI

app = FastAPI(title="ZYRA API CORE")

@app.get("/")
def root():
    return {"status": "ZYRA RUNNING"}
