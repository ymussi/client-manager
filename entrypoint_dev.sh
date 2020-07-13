#!/bin/bash

entrypoint(){
    # cd /app/wishlist/wishlist
    # # upgrade database
    # echo "upgrade database ...."
    # alembic upgrade head

    cd ..
    # run webserver
    echo "starting webserver ...."
    uwsgi --ini /app/wishlist/run.ini
}

entrypoint