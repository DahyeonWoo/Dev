# pip install uvicorn
# pip install "fastapi[all]"
# uvicorn src.main:app

from fastapi import FastAPI

app = FastAPI(
    title="FastAPI - Hi World code",
    description="This is the Hi World of FastAPI.",
    version="1.0.0",
)


@app.get("/")
def hi_world():
    return {"Hi": "World"}
