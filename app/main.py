from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def home():
    return {"Hellow":"World"}