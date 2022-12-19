## Extend the official Rasa SDK image
FROM rasa/rasa-sdk:latest

## Use subdirectory as working directory
WORKDIR /app

## Copy any additional custom requirements, if necessary (uncomment next line)
# COPY actions/requirements-actions.txt ./
USER root


## Copy actions folder to working directory
COPY ./actions /app/

RUN chgrp -R root /app/* && chmod -R 770 /app/*
## upgrade pip
# RUN python3 -m pip install --upgrade pip

## Install extra requirements for actions code, if necessary
# RUN pip install -r requirements.txt

## Change back to root user to install dependencies

## Run the action server (if you want to specify the port use this 
# instead: CMD ["start","--actions","actions", "--port", "xxxx" ]
# where xxxx  is the port you want to specify
CMD ["start", "--actions”, "actions”, "--port", "5055"]

## By best practices, don't run the code with root user
USER 1001