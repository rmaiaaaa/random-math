from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/math/sum/")
async def random_sum(number: int = 0):
    return{"message": number}
