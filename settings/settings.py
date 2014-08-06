# ----------------------------------------------------
# main settings for this project
# ----------------------------------------------------

import sys
from os import path

# add PROJECT_ROOT, libs and any required 3rd party folders
PROJECT_ROOT = path.dirname(path.abspath(__file__))
sys.path.append(path.join(PROJECT_ROOT, '../lib/'))

# ----------------------------------------------------

DEBUG = True

WINDOW = {
    'width': 100,
    'height': 200,
    'fullscreen': False,
    'vsync': True,
    'framerate': 60
}

# ----------------------------------------------------

# import local settigns
try:
    from settings_local import *
except ImportError, e:
    print 'Please add you settings/local.py file'
    sys.exit()
