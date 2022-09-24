from fastapi import FastAPI
from model import User
app = FastAPI()


@app.get("/service_2")
async def root():
    return {"message": "Hello From Service 2"}


@app.post('/service_2/usr')
def create_user(request:User):
    
   return {"res":request.username}
