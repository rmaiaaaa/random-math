from fastapi import FastAPI
from RandomMath import RandomMathOperations as RandomMath

app = FastAPI()
math = RandomMath.RandomMath()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/math/sum/")
async def random_sum(number: int = 0):
    return{"message": number}
