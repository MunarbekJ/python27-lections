from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "hello world"}

@app.get("/create")
def create():
    return{"message": "created"}

@app.delete("/delete")
def delete():
    return {"message": "deleted"}


