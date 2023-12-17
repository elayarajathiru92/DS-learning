#pip install fastapi
#pip install uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Add(BaseModel):
    n1: int
    n2: innt

@app.post("/add")
async def add(numbers: Add):
    sum = numbers.n1 + numbers.n2
    return {"result": sum}

if __name__ == "__main__":
    import uvicorn
 
    uvicorn.run(app)#, host="127.0.0.1", port=8000)
