from . base import *  #NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['47.115.88.138', '127.0.0.1']

STATIC_ROOT = os.path.join(BASE_DIR, 'static_ol')