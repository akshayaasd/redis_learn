from fastapi import FastAPI
import redis

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, db=0)

@app.get("/set/{key}/{value}")
def set_key(key: str, value: str):
    r.set(key, value)
    return {"message": f"{key} set to {value}"}

@app.get("/get/{key}")
def get_key(key: str):
    value = r.get(key)
    return {"value": value.decode() if value else "Key not found"}
