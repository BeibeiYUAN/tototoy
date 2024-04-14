# syntax=docker/dockerfile:1
# We recommend using docker/dockerfile:1, which always points to the latest release of the version 1 syntax. 

# Step 1. Define Base Image, Run apt-gets, Install Python
# The line following the syntax directive defines what base image to use:
FROM ubuntu:22.04
# Environment setup: The following line executes a build command inside the base image.
RUN apt-get update && apt-get install -y python3 python3-pip


# Step 2. Installing dependencies required by the Python application.
WORKDIR /application
COPY environment /application/environment
RUN pip install -r environment/requirements.txt 


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
ENV FLASK_APP=/application/app/app

# Exposed ports: The EXPOSE instruction marks that our final image has a service listening on port 8000.
EXPOSE 8000

# Starting the application: Finally, CMD instruction sets the command that is run when the user starts a container based on this image.
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]