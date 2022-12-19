# Extend the official Rasa SDK image
FROM rasa/rasa:latest

# RUN apt-get update && \
#       apt-get -y install sudo

# Use subdirectory as working directory
WORKDIR /app

# Copy code
COPY . .

# Change to root user to install dependencies
USER root

# Apply permissions to the rasa root directory
RUN chgrp -R root /app/* && chmod -R 770 /app/*

# Train a nlu whitout using the load models (uncomment if you dont have any models)
RUN rasa train nlu

# Set entrypoint for interactive shells
ENTRYPOINT [ "rasa" ]

# Command to run when the container is up
CMD ["run", "--enable-api", "--port", "5005"]

# By best practices, don't run the code with root user
USER 1001