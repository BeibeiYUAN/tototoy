#!/bin/sh

## When we build a docker image from the Dockerfile
## in this folder, it will run this script every
## time it starts. The command below starts
## our flask application behind the gunicorn
## wsgi server. Documentation on gunicorn can be
## found at https://docs.gunicorn.org/en/stable/


LOGGING_CFG_FILE="app/core/logging.conf"

# The default logging is to use JSON for the messages
# If you are working locally, you don't want this as
# it will put stacktraces on one long line
if [ "${DISABLE_JSON_LOGGING}" = "1" ]
then
    echo "Disabling all JSON style logging - should only be used locally!!"
    LOGGING_CFG_FILE="app/core/logging-json-disabled.conf"
fi


gunicorn \
  --config app/core/gunicorn_conf.py \
  --log-config ${LOGGING_CFG_FILE} \
  --timeout 600 \
  -b 0.0.0.0:8080 \
  app.wsgi:my_app
