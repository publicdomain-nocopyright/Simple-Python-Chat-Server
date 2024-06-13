# server.py - Asynchronous Chat Server

import sys
sys.dont_write_bytecode = True

from aiohttp import web
import aiosqlite

import library.relativePath


async def index(request):
    return web.FileResponse(library.relativePath + "/response/index.html")

# TODO: return .json file showing all registered routes that are not vulnerable to security
# INFO: Mostly to list the routes and display on the index page.
async def information(request):
    return web.FileResponse(library.relativePath + "/response/posting.html")

async def posting(request):
    return web.FileResponse(library.relativePath + "/response/posting.html")

# TODO: How to make it without redirect to another web page?
#   TODO: HTTP 204 No Content response.
#   TODO: - not giving the visual response to the user. 
#   TODO: Generate a new HTML page response.
# TODO: How to make it with Websockets?
# TODO: How to make authentication?
# TODO: How to upload images?
# TODO: How to provide Web API for interacting as user or bot in a chat?
# TODO: How to do end-to-end encryption?
# TODO: How to do a decentralized database?
# TODO: How to make a master server if it's a chat platform?
# TODO: User Registration: Save user information. 
# TODO: Make user login form.
# TODO: Make chat box.
# TODO: Add DDOS security.
# TODO: Create a project for crowdfunding.
# TODO: Add Emojis
# TODO: Add Images support
# TODO: Add Attachments server
# TODO: Add User Settings


import response.posting_success
#response.posting_success.posting_success()


async def save_text(request):
    data = await request.post()
    text = data.get('text')

    if text:
        async with aiosqlite.connect(databasefile) as db:
            await db.execute('CREATE TABLE IF NOT EXISTS texts (id INTEGER PRIMARY KEY, text TEXT)')
            await db.execute('INSERT INTO texts (text) VALUES (?)', (text,))
            await db.commit()
            modified_html = await response.posting_success.modify_html(library.relativePath + '/response/posting.html')
            return web.Response(text=modified_html, content_type='text/html')
            #return web.Response(status=204)  # HTTP 204 No Content response
        
    # Fetch all texts to display
    async with aiosqlite.connect('databasefile') as db:
        async with db.execute('SELECT id, text FROM texts') as cursor:
            rows = await cursor.fetchall()
            texts = [dict(id=row[0], text=row[1]) for row in rows]

if __name__ == '__main__':

    global databasefile
    databasefile = library.relativePath + '/serverdatabase.db' 
    
    import os
    db_path = os.path.abspath(databasefile)
    print(f"Database will be created at: {db_path}")
    print(f"Current working directory: {os.getcwd()}")

    # Serves Web Pages
    app = web.Application()
    app.add_routes([web.get('/', index)])
    app.add_routes([web.get('/posting', posting)])
    app.add_routes([web.post('/save-text', save_text)])
    web.run_app(app)