import os
import sys


relative_path = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.modules[__name__] = relative_path
