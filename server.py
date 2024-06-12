# server.py - Asynchonous Chat Server

from aiohttp import web

import sys
sys.dont_write_bytecode = True

import library.relativePath


async def index(request):
    return web.FileResponse(library.relativePath + "/library/index.html")

app = web.Application()
app.add_routes([web.get('/', index)])

if __name__ == '__main__':
  web.run_app(app)