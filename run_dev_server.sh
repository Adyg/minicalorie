#!/bin/bash

#require sudo
if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo:"
    echo "sudo $0 $*"
    exit 1
fi

cd /vagrant_data
printf "Installing requirements ...\n"
pip install -r requirements/local.txt

printf "Running collectstatic ...\n"
/usr/bin/python /vagrant_data/manage.py collectstatic --noinput --settings=minicalorie.settings.local
printf "Starting server on the box's port 8001 ...\n"
/usr/bin/python /vagrant_data/manage.py runserver [::]:8001 --settings=minicalorie.settings.local