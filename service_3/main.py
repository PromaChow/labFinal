from fastapi import FastAPI

from httpx import AsyncClient
import httpx
app = FastAPI()


@app.get("/service_3")
async def root():
    client_http = AsyncClient()
    token = {"user"}
    headers = {'user': token}
    
    response = await client_http.post('http://service_2:8000/service_2/usr' ,json = {"username":"proma", "password":"pro"})
    data = response.json()
    return {"message": data}


