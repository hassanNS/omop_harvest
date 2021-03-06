#!/bin/bash

# Install CHOP Authentication for CHOP/CID
cd /opt/apps/harvest-app/ && /opt/ve/harvest-app/bin/pip install -r /opt/apps/harvest-app/continuous_deployment/requirements.txt

cd /opt/apps/harvest-app/ && /opt/ve/harvest-app/bin/fab get_configuration:noinput=True

cd /opt/apps/harvest-app/ && make build
cd /opt/apps/harvest-app/ && make sass
cd /opt/apps/harvest-app/ && make collect
cd /opt/apps/harvest-app/ && /opt/ve/harvest-app/bin/python ./bin/manage.py syncdb --noinput
cd /opt/apps/harvest-app/ && /opt/ve/harvest-app/bin/python ./bin/manage.py migrate --noinput
cd /opt/apps/harvest-app/ && /opt/ve/harvest-app/bin/python ./bin/manage.py collectstatic --noinput
cd /opt/apps/harvest-app/ && /opt/ve/harvest-app/bin/python ./bin/manage.py rebuild_index --noinput
supervisord -c /opt/supervisor_run.conf -n
