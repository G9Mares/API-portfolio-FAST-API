from fastapi import FastAPI
app = FastAPI()
from dotenv import load_dotenv
import os
load_dotenv()

@app.get("/")
async def home():
    return {"Hellas":f"Men World {os.getenv('MI_VARIABLE')}"}