# Start with a python base image
# Take your pick from https://hub.docker.com/_/python
FROM python:3.11-slim

# Set /ai300-capstone as the main application directory
WORKDIR /ai300-capstone

# Copy the requirements.txt file and required directories into docker image
COPY ./requirements.txt /ai300-capstone/requirements.txt
COPY ./src /ai300-capstone/src
COPY ./model /ai300-capstone/model

# Add /src directory to PYTHONPATH, so that model.py Python module can be found
# To add multiple directories, delimit with colon e.g. /flask-app/src:/flask-app
ENV PYTHONPATH /ai300-capstone/src

# Install python package dependancies, without saving downloaded packages locally
RUN pip install -r /ai300-capstone/requirements.txt --no-cache-dir

# Allow port 80 to be accessed (Flask app)
EXPOSE 80

# Start the Flask app using gunicorn
CMD ["gunicorn", "--bind=0.0.0.0:80", "src.app:app"]