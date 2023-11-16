#!/bin/bash

docker run --rm -it -p 8080:8080 -e DISABLE_JSON_LOGGING=1 --env-file .env tototoy
