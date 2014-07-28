#!/bin/bash

service memcached start

# Install CHOP Authentication for CHOP/CID
cd /opt/apps/harvest-app/ && /opt/ve/harvest-app/bin/pip install http://github.research.chop.edu/cbmi/django-chopauth/archive/master.tar.gz

cd /opt/apps/harvest-app/ && /opt/ve/harvest-app/bin/fab get_configuration:noinput=True

cd /opt/apps/harvest-app/ && make build
cd /opt/apps/harvest-app/ && make sass
cd /opt/apps/harvest-app/ && make collect
cd /opt/apps/harvest-app/ && /opt/ve/harvest-app/bin/python ./bin/manage.py syncdb --noinput
cd /opt/apps/harvest-app/ && /opt/ve/harvest-app/bin/python ./bin/manage.py migrate --noinput
cd /opt/apps/harvest-app/ && /opt/ve/harvest-app/bin/python ./bin/manage.py collectstatic --noinput
cd /opt/apps/harvest-app/ && /opt/ve/harvest-app/bin/python ./bin/manage.py rebuild_index --noinput
supervisord -c /opt/supervisor_run.conf -n
