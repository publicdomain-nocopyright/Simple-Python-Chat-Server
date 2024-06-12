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


async def save_text(request):
    data = await request.post()
    text = data.get('text')

    if text:
        async with aiosqlite.connect(library.relativePath + '/serverdatabase.db') as db:
            import os
            db_path = os.path.abspath(library.relativePath + '/serverdatabase.db')
            print(f"Database will be created at: {db_path}")
            print(f"Current working directory: {os.getcwd()}")
            await db.execute('CREATE TABLE IF NOT EXISTS texts (id INTEGER PRIMARY KEY, text TEXT)')
            await db.execute('INSERT INTO texts (text) VALUES (?)', (text,))
            await db.commit()
            return web.Response(text="Text saved successfully")

if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/', index)])
    app.add_routes([web.get('/posting', posting)])
    app.add_routes([web.post('/save-text', save_text)])
    web.run_app(app)