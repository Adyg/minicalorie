env SECRET_KEY=`heroku config:get SECRET_KEY --app=minicalorie` \
    AWS_SECRET_ACCESS_KEY=`heroku config:get AWS_SECRET_ACCESS_KEY --app=minicalorie` \
    AWS_ACCESS_KEY_ID=`heroku config:get AWS_ACCESS_KEY_ID --app=minicalorie` \
    AWS_STORAGE_BUCKET_NAME=`heroku config:get AWS_STORAGE_BUCKET_NAME --app=minicalorie` \
    STATIC_ROOT='/vagrant/assets' \
    /usr/bin/python manage.py collectstatic --settings=minicalorie.settings.heroku
cd ..
