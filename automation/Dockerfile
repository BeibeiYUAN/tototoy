# syntax=docker/dockerfile:1

FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000

# ## This file is what tells Docker how to construct
# ## a reusable image of your application.
# ##
# ## Full description for various entries are provided
# ## below.
# ##
# ## In general, you should take care when deciding
# ## to merge to dockerfiles together; generally
# ## each is built for a specific purpose, and by
# ## design should that purpose should not be expanded
# ## unless absolutely necessary.

# FROM docker.binrepo.cglcloud.in/datascience/conda-base:ubuntu_20.04_py_3.10.12


# # Cargill Data Science @ 2020
# LABEL maintainer="jeremy gruel"
# ## Anything that is not expected to change very often
# ## (or at all) should go up here near the top of the
# ## dockerfile. See our fuller description below for
# ## the reasons why.
# WORKDIR /application

# ## When building locally, we need to tell pip to disable all of the
# ## checking for the main hosts
# ARG DISABLE_SSL_CONDA_AND_PIP

# ## These two settings make it so that logs from your
# ## application will be written as strings, and show up
# ## consistently in datadog.
# ENV PYTHONUNBUFFERED=TRUE
# ENV PYTHONDONTWRITEBYTECODE=TRUE

# ## This is our standard pattern for installing packages;
# ## We separate copying the 'environment' files (which are
# ## where dependencies live) from copying the rest of what
# ## we need further down, because this enables Docker to
# ## cache the install step between builds when the
# ## dependencies don't change.
# COPY environment /environment
# ## The broader mechanic is that if a given STEP (COPY, RUN,
# ## whatever) changes, everything down-file from that step
# ## is considered invalid and must be re-done. In this case,
# ## if you change something in the 'environment' folder
# ## without changing the code, Docker will -not- cache the
# ##     COPY . .
# ## step below and will still re-copy your code. But using
# ## this structure, if you change your code without changing
# ## the dependencies, everything -above- the
# ##     COPY . .
# ## can be cached. This can save you a lot of time when
# ## continually rebuilding your dockerfile to troubleshoot
# ## environment issues.
# ##
# ## Note that this will -not- affect builds in Drone,
# ## because Drone does not allow build-caching.



# COPY --from=0 /cloudera /cloudera_install





# ## A RUN block runs a SINGLE shell statement. Standard
# ## practice, as below, is to pack a bunch of functionality
# ## together into one statement with the '\' and '&&'
# ## shell operators.
# ##
# ## This allows us to do a lot of stuff while minimizing
# ## (as much as possible) the size of the resulting
# ## dockerfile. The heuristic here is, more toplevel
# ## statements (RUN, COPY, ADD, ENV, EXPORT, etc) means
# ## a bigger resulting image.
# ##
# ## Here, we check two sets of possible dependencies.
# ## First, if you have to depend on linux/system-level
# ## packages (like curl, or libxrender, that kind of thing)
# ## you can add them, one per line, to the file
# ##     environment/apt-packages.list
# ## When building the dockerfile, we will read that file
# ## and attempt to install every package listed from the
# ## debian package repositories.
# RUN echo >> /environment/apt-packages.list \
#   && apt-get -qq update \
#   && apt-get -qq install -y $(grep -v '^#' /environment/apt-packages.list) \
#   && apt-get install -qq -y /cloudera_install/clouderaimpalaodbc_2.6.7.1007-2_amd64.deb libgssapi-krb5-2 unixodbc \
#   && cp /cloudera_install/odbcinst.ini /etc \
#   && cp /cloudera_install/cloudera.impalaodbc.ini  /opt/cloudera/impalaodbc/lib/64 \
#   && cp /cloudera_install/cloudera.impalaodbc.ini /root \
#   && cp /cloudera_install/odbc.ini /root/.odbc.ini \
#   && cp /cloudera_install/odbc.ini /opt/cloudera/impalaodbc/Setup/ \
#   && rm -rf /cloudera_install \
#   ## Now also clean any temporary deb files created by apt-get
#   ## like the deb files
#   && apt-get clean \
#   && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
#   ## Next, we update the (base) conda environment using
#   ## the contents of your environment file:
#   ##     environment/environment.yml
#   ## We update the (base) environment because (base) is
#   ## active by default, and by design we expect that a
#   ## Docker image built from this file will only ever be
#   ## used for one thing, and so only needs the one environment.
#   ## Also set the timeouts to 900 seconds for all connections that are made
#   && if [ "${DISABLE_SSL_CONDA_AND_PIP}" = "1" ] ; then echo "Disabling SSL checks for pip and conda" ; pip config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org" && pip config set global.timeout 900  && conda config --set ssl_verify False && conda config --set remote_read_timeout_secs 900 ; fi \
#   && conda env update --name base --file /environment/deploy.environment.yml --quiet \
#   ##
#   ## Now clean up all temporary files
#   && conda clean -q -y -a \
#   ## Use the combination with true here to ensure we don't halt the chain if no pip packages installed
#   && (pip cache purge ; true) \
#   ## Note that we use ONLY the 'environment.yml' file. We will
#   ## NOT use 'dev.environment.yml', and we will NOT use any
#   ## files generated raw by templates, like:
#   ##     - flask.environment.yml
#   ##     - core.environment.yml
#   ## because those are intended for you to -merge- into your
#   ## 'environment.yml' file.
#   ##
#   ## Lastly, we remove the entire 'environment' directory from
#   ## the built image, because it's easy and reduces the final
#   ## image size.
#   && rm -rf /environment

# ## Here we copy EVERYTHING from the current directory into
# ## this image. Note that the function of this call is modified
# ## by the presence of a '.dockerignore' file in the current
# ## directory. When following standard practice and running
# ## this file from the root of your project:
# ##     docker build . -f automation/Dockerfile
# ## the .dockerignore file provided by your various templates
# ## should stop us from adding anything we don't actually need.
# ##
# ## Do make sure you have merged this template's version of
# ## the .dockerignore file into yours, though, or your builds
# ## will be much larger than they should be.
# COPY . .

# ## Importantly, note that we include everything in 'science/models'
# ## but that we EXCLUDE 'science/notebooks' and 'science/data'.
# ## We do this intentionally! The image doesn't need your
# ## notebooks, and we expect your data to be huge, and the
# ## bigger your Docker image is, the more likely that
# ## it will just -fail- to build in Drone, because one step
# ## or another will time out.


# ## For all windows users, when building docker images locally the
# ## bash script automation/entrypoint.sh will have dos style line
# ## endings. Convert them to unix style endings
# RUN sed -i 's/\r//' /application/automation/entrypoint.sh

# ## The ENTRYPOINT and CMD directives are used together to
# ## tell Docker what to do in order to 'run' our Docker image
# ## Either can be used alone, but using them together as we
# ## do here is considered best practice because it provides
# ## specific functionality. If we run the image built from
# ## this dockerfile with no arguments:
# ##
# ##     docker run this-image
# ##
# ## the image will start by invoking the following command:
# ##
# ##     bash /entrypoint.sh
# ##
# ## If we run the image built from this dockerfile -with-
# ## arguments:
# ##
# ##     docker run this-image some-arg
# ##
# ## those arguments will be passed to our script:
# ##
# ##     bash /entrypoint.sh some-arg
# ##
# ## In general, we recommend not configuring or passing
# ## arguments in this fashion, but we still provide you
# ## the option to do that here, in case the need arises.
# ENTRYPOINT ["bash", "/application/automation/entrypoint.sh"]
# ## We put an 'empty' CMD directive here to make sure that
# ## we are overriding any CMD directives that might be
# ## defined upstream, because their contents will be passed
# ## as arguments to the ENTRYPOINT directive above.
# ## In this case, the default entrypoint script does not
# ## expect to receive any arguments, so we ensure that we
# ## are passing none in order to avoid unexpected behavior.
# CMD []
