# ComputerVisionRestAPI

## Project Overview
`ComputerVisionRestAPI` is a Python projects that allows users to identify the coordinates of the rectangular box localizing a face. Users can send a HTTP POST request with an image attached to the server, and receive back the 4 coordinates of this rectangle. In addition, this project also include a Client program to make it easier for users to send the image without the hassle of coding.

## Components:

This project includes the below component:
- A REST API Server written in Python using Flask library
- A REST API Client to send the POST request to the server
- A built-in SQL lite database to record the requests sent
- Heroku integration to showcase the server
- A Docker image

## Dependencies:

- For the Server, please run the below command to install dependencies from [ComputerVisionServer.yml](ComputerVisionServer.yml):
```bash
$ conda env create -f ComputerVisionServer.yml
```

- For the Client, please run the below command to install dependencies from [ComputerVisionClient.yml](ComputerVisionClient.yml):
```bash
$ conda env create -f ComputerVisionClient.yml
```

## Server commands:

- Start the server:
```bash
$ export FLASK_APP=src/app.py
$ python -m flask run
```

- Go to the home page (port 80) to see the list of requests.

## Client commands:

```bash
$ python src/client.py --api='http://<your_host>:80/recognizeFace' --img_path=<your_path_to_image>
```

## Heroku Integration:

Please go to this [Heroku website](https://cv-face-recognition.herokuapp.com/) to see the list of requests sent there. In addition, you can send your http request to this host.

## Docker image

Please go to this [Docker website](https://hub.docker.com/r/tdkhanhvu/cv-face-recognition) to pull a Docker image of this project.
