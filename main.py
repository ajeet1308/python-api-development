from fastapi import FastAPI
from router import post_router

app = FastAPI()

@app.get("/")
def root():
    return {"message":"welcome to my api"}

app.include_router(post_router)