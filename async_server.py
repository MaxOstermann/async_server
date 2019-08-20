from aiohttp import web, ClientSession
import asyncio
from urllib.parse import urljoin
import json


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_client(url):
    async with ClientSession() as session:
        json_data = await fetch(session, url)
        data = json.loads(json_data)
        return data


async def handle_intro(request):
    json_data = await request.text()
    data = json.loads(json_data)
    url_cli = urljoin("http://api.test.brn.pw/clients/", data["client_id"])
    client = await get_client(url_cli)
    url_tar = urljoin("http://api.test.brn.pw/tariffs/", data["tariff_id"])
    tariff = await get_client(url_tar)
    tariff_by_user = {
        "id": 6,
        "success": True,
        "status": "TRIAL",
        "tariff": tariff,
        "client":{
            "id": client["id"],
            "name": client["name"],
            "username": client["username"],
            "email": client["email"]
        }
    }
    return web.json_response(tariff_by_user)


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('POST', '/', handle_intro)

    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8080)
    print("Server started at http://127.0.0.1:8080")
    return srv


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
