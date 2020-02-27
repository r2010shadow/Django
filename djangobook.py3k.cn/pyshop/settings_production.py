from .settings import *
import socket




if socket.gethostname() == 'Matrix.local':
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
else:
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG


