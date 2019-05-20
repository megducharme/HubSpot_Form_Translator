#!/bin/sh

exec gunicorn -w 3 -b 0.0.0.0:8084 NssApplications.wsgi
