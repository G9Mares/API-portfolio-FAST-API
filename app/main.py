from fastapi import FastAPI
import os

app = FastAPI()
@app.get("/")
async def home():
    return {"Hellas":f"Men s World {os.getenv('MI_VARIABLE')}"}