from fastapi import FastAPI

app = FastAPI()


@app.get("/service_1")
async def root():
    return {"message": "Hello World"}