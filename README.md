# ComputerVisionRestAPI

## Project Overview
`ComputerVisionRestAPI` is a Python projects that allows users to identify the coordinates of the rectangular box localizing a face. Users can send a HTTP POST request with an image attached to the server, and receive back the 4 coordinates of this rectangle. In addition, this project also includes a Client program to make it easier for users to send the image without the hassle of coding.

## Components:

This project includes the below components:
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

## Future Improvements

Due to the time constraint, I have chosen the lightweight frameworks / components to build this project. As a result, below are the few considerations to further enhance the performance and security of this project:

**1. Replace the web framework**

Some of the drawbacks of Flask are: unsuitable for big applications, no admin site, potentially challenging migration... Therefore, we can consider other full-fledged frameworks such as Django to substitute Flask.

**2. Replace the database**

SQLite can only handle low to medium traffic HTTP requests, and its database size is restricted to 2GB in most cases. Hence, we can contemplate switching to other powerful Databases such as MySQL or PostgreSQL if there is an increase in demand for this service.

**3. Develop a separate portal to display requests**

We should introduce a separate web page with authentication to display requests sent to this website.

**4. Replace the Pillow library used**

I used the Pillow library to convert the data sent to the server into an image. Nevertheless, I had some trouble trying to package this project into a Docker image. It took me a few hours to troubleshoot this problem, and fortunately, I managed to find a sample Dockerfile on a Github repository listing the necessary dependencies to build Pillow. The same problem did not occur when installing using Conda locally or Pip on Heroku web page.

**5. Reduce the size of the Docker image and optimize the Dockerfile**

Due to the problem in point 4 above, I had to list quite a number of dependencies and this probably led to a huge Docker image of 1GB despite the simplicity of this project. Further work can be done to trim this Docker image.

**6. Introduce other features to analyze the pictures sent**

For now, I only focus on finding the rectangle surrounding the face. However, we can introduce other Rest API Endpoints such as to detect the remaining items in the background, or predicting the gender, age, race... of the person.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/tdkhanhvu/ComputerVisionRestAPI/graphs/contributors).

- Tran Doan Khanh Vu