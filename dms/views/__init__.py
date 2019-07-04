from sanic.request import Request
from sanic import response


async def ping(request: Request):
    return response.text('pong!')
