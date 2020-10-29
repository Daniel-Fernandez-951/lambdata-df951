# Select Base Image from Docker-Hub
FROM ubuntu

# Possibly not needed in regular deployment, used for python logging in playground
ENV PYTHONBUFFER=1

# List of terminal commands
RUN apt update && \
    apt upgrade -y && \
    apt install python3 python3-pip curl -y && \
    pip3 install pandas numpy
    pip3 install -i https://test.pypi.org/simple/ lamdata-df951