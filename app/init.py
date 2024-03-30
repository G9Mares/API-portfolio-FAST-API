import os
from dotenv import load_dotenv
import uvicorn



load_dotenv()
if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, port=80, host="0.0.0.0")