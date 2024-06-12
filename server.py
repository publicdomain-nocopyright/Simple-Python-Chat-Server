# server.py - Asynchonous Chat Server

import sys
sys.dont_write_bytecode = True

from aiohttp import web

import library.header 
import library.relativePath
library.header
#print(library.relativePath.getCurrentProjectPath())
import library.relativePath
print(library.relativePath)
async def index(request):
    return web.FileResponse(library.relativePath + "/index.html")

app = web.Application()
app.add_routes([web.get('/', index)])

if __name__ == '__main__':
  web.run_app(app)