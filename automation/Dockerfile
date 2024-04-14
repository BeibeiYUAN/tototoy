# syntax=docker/dockerfile:1

FROM node:18-alpine
WORKDIR /application


## When building locally, we need to tell pip to disable all of the
## checking for the main hosts
ARG DISABLE_SSL_CONDA_AND_PIP


## This is our standard pattern for installing packages;
## We separate copying the 'environment' files (which are
## where dependencies live) from copying the rest of what
## we need further down, because this enables Docker to
## cache the install step between builds when the
## dependencies don't change.
COPY environment /environment


# Now install pipenv and all of the dependencies with pipenv
RUN if [ "${DISABLE_SSL_FOR_PIP}" = "1" ] ; then echo "Disabling SSL checks for pip" ; pip config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org binrepo.cglcloud.in" && pip config set global.timeout 900 ; fi \
  ## In case of runnings locally in docker, allow for disabling ssl
  ## Generate empty Pipfile
  && echo "\n\n********************************************************************************\n*** Installing pipenv\n********************************************************************************" \
  && pip install pipenv \
  && echo "\n\n********************************************************************************\n*** Initializing pipenv\n********************************************************************************" \
  && pipenv install \
  && rm Pipfile.lock \
  ## If we want to disable ssl checks (building locally) we must modify verify_ssl in config
  && if [ "${DISABLE_SSL_FOR_PIP}" = "1" ] ; then sed -i 's/verify_ssl = true/verify_ssl = false/g' Pipfile ; fi \
  ## Generate the Pipfile and  Pipfile.lock
  && echo "\n\n********************************************************************************\n*** Installing packages from requirements.txt\n********************************************************************************" \
  && if [ "${DISABLE_SSL_FOR_PIP}" = "1" ] ; then echo "\n\n\n*** LOCAL BUILD NOTE ***\n\nYou have disabled SSL checks, but the way pipenv works is that it will still give\nexplicit warnings it is disabling SSL. Please discard red WARNING lines below\n\n\n" ; fi \
  && pipenv install --extra-pip-args "--dry-run"  -r /application/environment/requirements.txt  \
  && echo "\n\n********************************************************************************\n*** Installing all packages in the system wide python installation\n********************************************************************************" \
  && pipenv install --system \
  ##
  ## Now clean up all temporary files
  ## Use the combination with true here to ensure we don't halt the chain if no pip packages installed
  && (pip cache purge ; true)

## Here we copy EVERYTHING from the current directory into
## this image. Note that the function of this call is modified
## by the presence of a '.dockerignore' file in the current
## directory. When following standard practice and running
## this file from the root of your project:
##     docker build . -f automation/Dockerfile
## the .dockerignore file provided by your various templates
## should stop us from adding anything we don't actually need.
##
## Do make sure you have merged this template's version of
## the .dockerignore file into yours, though, or your builds
## will be much larger than they should be.
COPY . .

## For all windows users, when building docker images locally the
## bash script automation/entrypoint.sh will have dos style line
## endings. Convert them to unix style endings
RUN sed -i 's/\r//' /application/automation/entrypoint.sh\
    # Finally, clean up the environment files
    && rm -rf /application/environment


# Set the entrypoint for the docker image to be bash and provide the entrypoint shell
# script as the argument. This means whenever a container is started withour any
# arguments, docker will start running the entrypoint.sh script.
ENTRYPOINT ["bash", "/application/automation/entrypoint.sh"]

CMD []
EXPOSE 3000
