#!/bin/bash

docker-compose build
# docker-compose run apphost manage.py collectstatic --no-input
# docker build -t stevebrownlee/hubspotapps .
docker tag `docker images | grep 'hubspot_form_translator_apphost' | awk '{ print $3 }'` stevebrownlee/hubspotapps
