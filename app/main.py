import os
import json
import requests
import redis
import datetime
from typing import Optional, List
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()
crud_array_domain = os.environ.get("CRUD_ARRAY_DOMAIN","crud_array")
service_sort_domain = os.environ.get("SERVICE_SORT_DOMAIN","service_sort")
redis_domain = os.environ.get("REDIS_DOMAIN","redis")

@app.get("/mainRequest/{req_id}")
def main_request(req_id:str):
    '''
    1. DONE_взять рек_айди
    2. DONE_отправить запрос в сервис крудАррэй
    3. DONE_получить оттуда аррэй
    4. отправить аррэй в сервисСорт
    5. получить отсортированный аррэй
    6. вернуть результат "пользователю"
    '''
    redis_client = redis.Redis(host=redis_domain)
    redis_client.set(datetime.datetime.now().isoformat(),req_id)
    array12 = requests.get(f'http://{crud_array_domain}/array/{req_id}').json()
    return requests.post(f'http://{service_sort_domain}/sort',data=json.dumps(array12)).json()