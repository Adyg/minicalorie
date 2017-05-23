#!/bin/bash

#require sudo
if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo:"
    echo "sudo $0 $*"
    exit 1
fi

#update the solr schema
/usr/bin/python /vagrant_data/manage.py build_solr_schema -f /var/solr/collection1/conf/schema.xml
#schema updates require a solr restart
service solr restart
#reindex content
/usr/bin/python /vagrant_data/manage.py rebuild_index