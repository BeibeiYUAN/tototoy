#!/bin/bash

docker build --build-arg DISABLE_SSL_CONDA_AND_PIP=1 -t tototoy -f automation/Dockerfile .
