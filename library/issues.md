
#### AIOHTTP relative paths support
The AIOHTTP does not seem to respond to relative path.  
```
async def index(request):
    return web.FileResponse("./index.html")
```
I tried this and it just says it does not find the file.


#### Python __pycache__ the dont_write_bytecode as separate module does not work
dont_write_bytecode needs to be at the top a the main script file.  
If you are importing this functionality, the import itself still makes .pyc file before executing dont_write_bytecode
Therefore creating a pyCache for itself, and prevents only other .py imports from producing .pyc.
