import os
<<<<<<< HEAD
from global_settings import *

try:
    from local_settings import *
except ImportError:
    import warnings
    warnings.warn('Local settings have not been found (src.conf.local_settings)')

# If chopauth is available, import those settings
try:
    from chopauth.settings import *
except ImportError:
    pass

# FORCE_SCRIPT_NAME overrides the interpreted 'SCRIPT_NAME' provided by the
# web server. since the URLs below are used for various purposes outside of
# the WSGI application (static and media files), these need to be updated to
# reflect this alteration
if FORCE_SCRIPT_NAME:
    ADMIN_MEDIA_PREFIX = os.path.join(FORCE_SCRIPT_NAME, ADMIN_MEDIA_PREFIX[1:])

    STATIC_URL = os.path.join(FORCE_SCRIPT_NAME, STATIC_URL[1:])
    MEDIA_URL = os.path.join(FORCE_SCRIPT_NAME, MEDIA_URL[1:])

    LOGIN_URL = os.path.join(FORCE_SCRIPT_NAME, LOGIN_URL[1:])
    LOGOUT_URL = os.path.join(FORCE_SCRIPT_NAME, LOGOUT_URL[1:])
    LOGIN_REDIRECT_URL = os.path.join(FORCE_SCRIPT_NAME, LOGIN_REDIRECT_URL[1:])
=======
import json
from base import *
from app import *
import dj_database_url

try:
    from chopauth.settings import *
except ImportError:
    pass

curdir = os.path.dirname(os.path.abspath(__file__))
project_settings = json.loads(open(os.path.join(curdir, '../../.project_config.json'), 'r').read())['project_settings']

environment = get_env_variable('APP_ENV')

if environment not in project_settings.keys():
    error_msg = "Settings for {0} environment not found in project configuration.".format(environment)
    raise ImproperlyConfigured(error_msg)

# Check here to see if db details exist in env
LINKED_DB_IP = os.environ.get('DB_PORT_5432_TCP_ADDR')
# Check here to see if memcache details exist in env
LINKED_MEMCACHE = os.environ.get('MC_PORT_11211_TCP_ADDR')

if LINKED_DB_IP:
    DATABASES = {
        'default': dj_database_url.parse('postgresql://docker:docker@{0}:5432/omop_harvest'.format(LINKED_DB_IP)),
        'portal': dj_database_url.parse(project_settings[environment]['databases']['portal']),
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(project_settings[environment]['databases']['default']),
    }


if LINKED_MEMCACHE:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '{0}:11211'.format(LINKED_MEMCACHE),
            'KEY_PREFIX': 'omop_harvest',
            'VERSION': 1,
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique',
            'KEY_PREFIX': 'omop_harvest',
            'VERSION': 1,
        }
    }

EMAIL_PORT = project_settings[environment]['django']['EMAIL_PORT']

EMAIL_SUBJECT_PREFIX = '[OMOP Harvest] '

DEBUG = project_settings[environment]['django']['DEBUG']

FORCE_SCRIPT_NAME = project_settings[environment]['django']['FORCE_SCRIPT_NAME']

SECRET_KEY = project_settings[environment]['django']['SECRET_KEY']

# LDAP
LDAP = {}
LDAP['DEBUG'] = project_settings[environment]['django']['LDAP']['DEBUG']
LDAP['PREBINDDN'] = project_settings[environment]['django']['LDAP']['PREBINDDN']
LDAP['SEARCHDN'] = project_settings[environment]['django']['LDAP']['SEARCHDN']
LDAP['SEARCH_FILTER'] = project_settings[environment]['django']['LDAP']['SEARCH_FILTER']
LDAP['SERVER_URI'] = project_settings[environment]['django']['LDAP']['SERVER_URI']
LDAP['PREBINDPW'] = project_settings[environment]['django']['LDAP']['PREBINDPW']

REGISTRATION_MODERATORS = project_settings[environment]['django']['REGISTRATION_MODERATORS']
>>>>>>> 0e24556... Adding Containerization (Docker) and Subfolder for Continuous Integration and Deployment (CID)
