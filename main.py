from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello world"}

class HelloNameResp(BaseModel):
    message: str

@app.get('/hello/{name}', response_model=HelloNameResp) #dynamiczne adresy
def hello_name(name: str):
    return HelloNameResp(message=f"Hello {name}")
