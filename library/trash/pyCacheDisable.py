import sys
sys.dont_write_bytecode = True

import sys
import os

def cacheDisable():
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
    sys.dont_write_bytecode = True
    print("test")

cacheDisable()
#sys.modules[__name__] = cacheDisable()