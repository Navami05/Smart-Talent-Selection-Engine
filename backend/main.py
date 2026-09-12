from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Smart Talent Selection Engine API is running"
    }