#!/bin/bash

set -e

echo "${0}: running migrations."
python pixmessages/manage.py makemigrations
python pixmessages/manage.py migrate