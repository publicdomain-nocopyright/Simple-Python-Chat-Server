# server.py - Asynchronous Chat Server

import sys
sys.dont_write_bytecode = True

from aiohttp import web
import aiosqlite

import library.relativePath


async def index(request):
    return web.FileResponse(library.relativePath + "/library/index.html")

async def posting(request):
    return web.FileResponse(library.relativePath + "/library/posting.html")

# TODO: How to make it without redirect to another web page?
# TODO: How to make it with Websockets?
# TODO: How to make authentication?
# TODO: How to upload images?
# TODO: How to provide Web API for interacting as user or bot in a chat?
# TODO: How to do end-to-end encryption?
# TODO: How to do a decentralized database?
# TODO: How to make a master server if it's a chat platform?

async def save_text(request):
    data = await request.post()
    text = data.get('text')

    if text:
        async with aiosqlite.connect(databasefile) as db:
            await db.execute('CREATE TABLE IF NOT EXISTS texts (id INTEGER PRIMARY KEY, text TEXT)')
            await db.execute('INSERT INTO texts (text) VALUES (?)', (text,))
            await db.commit()
            return web.Response(text="Text saved successfully")

if __name__ == '__main__':

    global databasefile
    databasefile = library.relativePath + '/serverdatabase.db' 
    
    import os
    db_path = os.path.abspath(databasefile)
    print(f"Database will be created at: {db_path}")
    print(f"Current working directory: {os.getcwd()}")

    app = web.Application()
    app.add_routes([web.get('/', index)])
    app.add_routes([web.get('/posting', posting)])
    app.add_routes([web.post('/save-text', save_text)])
    web.run_app(app)