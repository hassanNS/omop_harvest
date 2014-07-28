# Harvest

FROM phusion/baseimage

MAINTAINER Le Mar Davidson "davidsonl2@email.chop.edu"

# Base Harvest System Software
RUN apt-get update -qq --fix-missing
RUN apt-get install -y curl python-dev python-setuptools supervisor git-core libpq-dev libsasl2-dev libldap2-dev openssl memcached curl python-dev python-setuptools supervisor git-core libpq-dev libldap2-dev libsasl2-dev build-essential libssl-dev redis-server libxml2-dev libxslt1-dev  zlib1g-dev wget ruby
RUN easy_install pip
RUN pip install virtualenv
RUN pip install uwsgi
RUN virtualenv --no-site-packages /opt/ve/harvest-app

# Base Harvest Python dependencies
RUN /opt/ve/harvest-app/bin/pip install "django==1.5.6"
RUN /opt/ve/harvest-app/bin/pip install "dj-database-url==0.2.2"
RUN /opt/ve/harvest-app/bin/pip install "south==0.8.4"
RUN /opt/ve/harvest-app/bin/pip install "fabric==1.8.0"
RUN /opt/ve/harvest-app/bin/pip install "uWSGI"
RUN /opt/ve/harvest-app/bin/pip install "restlib2==0.3.9"
RUN /opt/ve/harvest-app/bin/pip install "python-etcd==0.3.0"
RUN /opt/ve/harvest-app/bin/pip install "psycopg2==2.5.1"
RUN /opt/ve/harvest-app/bin/pip install "python-ldap==2.4.13"
RUN /opt/ve/harvest-app/bin/pip install "pycrypto==2.3"
RUN /opt/ve/harvest-app/bin/pip install "avocado>=2.3.0,<2.4"
RUN /opt/ve/harvest-app/bin/pip install "serrano>=2.3.0,<2.4"
RUN /opt/ve/harvest-app/bin/pip install "modeltree>=1.1.7,<1.2"
RUN /opt/ve/harvest-app/bin/pip install "django-haystack>=2.0"
RUN /opt/ve/harvest-app/bin/pip install "python-memcached==1.53"
RUN /opt/ve/harvest-app/bin/pip install "django_extensions"
RUN /opt/ve/harvest-app/bin/pip install "django-siteauth==0.9b1"
RUN /opt/ve/harvest-app/bin/pip install "whoosh>=2.5"
RUN /opt/ve/harvest-app/bin/pip install "Markdown"
RUN /opt/ve/harvest-app/bin/pip install "pycap"
RUN /opt/ve/harvest-app/bin/pip install "csvkit"

# Anything run after the "Add" command is not cached.
ADD continuous_deployment/configuration/supervisor_deploy.conf /opt/supervisor_deploy.conf
ADD continuous_deployment/configuration/supervisor_run.conf /opt/supervisor_run.conf
ADD continuous_deployment/scripts/start.sh /usr/local/bin/start
ADD continuous_deployment/scripts/test.sh /usr/local/bin/test
ADD continuous_deployment/scripts/etl.sh /usr/local/bin/etl
ADD continuous_deployment/scripts/debug.sh /usr/local/bin/debug
ADD continuous_deployment/scripts/heartbeat.sh /usr/local/bin/heartbeat

RUN chmod +x /usr/local/bin/debug
RUN chmod +x /usr/local/bin/start
RUN chmod +x /usr/local/bin/test
RUN chmod +x /usr/local/bin/heartbeat
RUN chmod +x /usr/local/bin/etl


# Scala needed for DataExpress scripts
RUN apt-get update -qq
RUN apt-get install -y openjdk-6-jre libjansi-java
RUN curl -O http://www.scala-lang.org/files/archive/scala-2.9.3.deb
RUN dpkg -i scala-2.9.3.deb
RUN apt-get update
RUN apt-get install -y scala

RUN (cd /tmp && git clone https://github.com/joyent/node.git)
RUN (cd /tmp/node && git checkout v0.10.26 && ./configure && make && make install)
RUN (apt-get install -y npm)
RUN (npm install -g coffee-script)
RUN apt-get update -qq --fix-missing
RUN gem install rubygems-update    &&  \
    update_rubygems                &&  \
    gem install sass bourbon

# Python dependencies

RUN /opt/ve/harvest-app/bin/pip install django==1.5.5
RUN /opt/ve/harvest-app/bin/pip install south==0.8.2
RUN /opt/ve/harvest-app/bin/pip install python-memcached==1.48
RUN /opt/ve/harvest-app/bin/pip install coverage
RUN /opt/ve/harvest-app/bin/pip install django-siteauth==0.9b1
RUN /opt/ve/harvest-app/bin/pip install raven==3.3.9
RUN /opt/ve/harvest-app/bin/pip install uwsgi
RUN /opt/ve/harvest-app/bin/pip install rq==0.3.8
RUN /opt/ve/harvest-app/bin/pip install django-rq==0.5.1
RUN /opt/ve/harvest-app/bin/pip install rq-dashboard==0.3.1
RUN /opt/ve/harvest-app/bin/pip install django-rq-dashboard
RUN /opt/ve/harvest-app/bin/pip install dj-database-url==0.2.2
RUN /opt/ve/harvest-app/bin/pip install south==0.8.4
RUN /opt/ve/harvest-app/bin/pip install fabric==1.8.0
RUN /opt/ve/harvest-app/bin/pip install uWSGI
RUN /opt/ve/harvest-app/bin/pip install restlib2==0.3.9
RUN /opt/ve/harvest-app/bin/pip install python-etcd==0.3.0
RUN /opt/ve/harvest-app/bin/pip install psycopg2==2.5.1
RUN /opt/ve/harvest-app/bin/pip install python-ldap==2.4.13
RUN /opt/ve/harvest-app/bin/pip install pycrypto==2.3
RUN /opt/ve/harvest-app/bin/pip install avocado==2.3.0
RUN /opt/ve/harvest-app/bin/pip install serrano==2.3.0
RUN /opt/ve/harvest-app/bin/pip install modeltree==1.1.7
RUN /opt/ve/harvest-app/bin/pip install django-haystack==2.0
RUN /opt/ve/harvest-app/bin/pip install python-memcached==1.53
RUN /opt/ve/harvest-app/bin/pip install django_extensions
RUN /opt/ve/harvest-app/bin/pip install django-siteauth==0.9b1
RUN /opt/ve/harvest-app/bin/pip install whoosh==2.5
RUN /opt/ve/harvest-app/bin/pip install Markdown
RUN /opt/ve/harvest-app/bin/pip install pycap
RUN /opt/ve/harvest-app/bin/pip install csvkit

# Upgrades
RUN /opt/ve/harvest-app/bin/pip install -U "avocado>=2.3.0,<2.4.0" "whoosh>=2.6,<2.7" "django-haystack>=2.0,<2.2"

# Add the application files
ADD . /opt/apps/harvest-app

# Ensure all python requirements are met
ENV APP_NAME omop_harvest
RUN /opt/ve/harvest-app/bin/pip install -r /opt/apps/harvest-app/requirements.txt --use-mirrors

# Add custom start script for continuous deployment/override default
ADD continuous_deployment/custom/scripts/start.sh /usr/local/bin/start

# Add custom script for loading an initial database
ADD continuous_deployment/data_service/scripts/load_initial_data.sh /usr/local/bin/load_initial_data

RUN chmod +x /opt/apps/harvest-app/run-tests.sh

RUN chmod +x /usr/local/bin/start

ENV ETCD_HOST ''

EXPOSE 8000
