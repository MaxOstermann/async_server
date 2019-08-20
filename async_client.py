import aiohttp
import asyncio
import json


"""
    Пример запроса
    {
        "client_id": "1",
        "tariff_id": "1"
    }
"""
async def fetch(session, url):
    data = {
        "client_id": "1",
        "tariff_id": "1"
    }
    async with session.post(url, data=json.dumps(data)) as response:
        return await response.text()
"""
    Пример ответа
    {
    "id": 6,
    "success": true,
    "status": "TRIAL",
    "tariff": {
        "id": 1,
        "name": "One website (100MB)",
        "size": 100,
        "websites": 1,
        "databases": 10
    },
    "client": {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    }
    }
"""


async def main():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, 'http://127.0.0.1:8080')
        print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
