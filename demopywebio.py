from fastapi import FastAPI
from pywebio.platform.fastapi import webio_routes
import uvicorn
from pywebio.output import *

app = FastAPI()

def task_func():
    put_text("test")

@app.get("/app")
def read_main():
   return {"message": "Hello World from main app"}

# `task_func` is PyWebIO task function
app.mount("/tool", FastAPI(routes=webio_routes(task_func)))

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)