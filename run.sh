#!/bin/bash

if [ -z $1 ]
then
  docker run -d -it -p 8000:8084 stevebrownlee/hubspotapps

else
  docker run -p 80:8084 stevebrownlee/hubspotapps

fi

