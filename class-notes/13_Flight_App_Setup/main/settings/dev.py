from .base import *

THIRD_PARTY_APPS = ["debug_toolbar"] 
 
DEBUG = True 
 
INSTALLED_APPS += THIRD_PARTY_APPS 
 
THIRD_PARTY_MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] 
 
MIDDLEWARE += THIRD_PARTY_MIDDLEWARE 
 

 
INTERNAL_IPS = [ 
    "127.0.0.1", 
]