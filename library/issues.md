
#### AIOHTTP relative paths support
The AIOHTTP does not seem to respond to relative path.  
```
async def index(request):
    return web.FileResponse("./index.html")
```
I tried this and it just says it does not find the file.