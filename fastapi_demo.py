import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home(name: str):
    return {"message": f"Hello! {name}"}
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)