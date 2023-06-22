FROM python:3.10.11

# Update APT
RUN apt-get update

# Make work directory
RUN mkdir /app
WORKDIR /app

# Install required packaged for Dijango projects
COPY ./server/requirements.txt ./app/server/requirements.txt
RUN pip install -r ./app/server/requirements.txt

# Clone source code
COPY . .

# Expose FastApi Server Port
EXPOSE 8008

# Start webserver
CMD ["uvicorn", "server.main:app", "--host=0.0.0.0", "--reload"]