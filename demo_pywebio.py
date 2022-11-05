from fastapi import FastAPI
from pywebio.platform.fastapi import webio_routes
import uvicorn
from pywebio.output import *

app = FastAPI()

def pywebio():
    put_text("test")

@app.get("/fastapi")
def read_main():
   return {"message": "Hello World from main app"}

# `task_func` is PyWebIO task function
app.mount("/pywebio", FastAPI(routes=webio_routes(pywebio)))

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=3000)