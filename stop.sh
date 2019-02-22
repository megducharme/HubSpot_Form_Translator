#!/bin/bash

docker stop `docker ps | grep 'stevebrownlee/hubspotapps' | awk '{ print $1 }'`

