from fastapi import FastAPI

app = FastAPI()

@app.get("/get")
def home():
    return {"message": "working"}