import aiohttp
import asyncio
import json


async def fetch(session, url):
    data = {
        "client_id": "1",
        "tariff_id": "1"
    }
    async with session.post(url, data=json.dumps(data)) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://127.0.0.1:8080')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
