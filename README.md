# Welcome to Image Classification

This application is image classification inference, a target application of our research study as machine learning inference. This implementation is developed in Python using [Flask](https://flask.palletsprojects.com/en/stable/), a lightweight Web Server Gateway Interface (WSGI) web application framework, used to forward requests from a web server to a backend application or framework, and deployed on a Kubernetes cluster hosted by [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/). Additionally, a [pretrained model](https://pytorch.org/vision/main/models.html) from [PyTorch](https://pytorch.org/) is integrated and deployed as a service. Based on the list of pre-trained models in PyTorch,
[EfficientNet_B3](https://pytorch.org/vision/stable/models/generated/torchvision.models.efficientnet_b3.html#torchvision.models.EfficientNet_B3_Weights) is selected due to its high accuracy of 96.054% and relatively small file size of 47.2 MB.

## About Project

A research under a title of `Adaptive Horizontal Pod Autoscaling (AHPA) Based on Reinforcement Learning in Kubernetes for Machine Learning`, introducing the Adaptive Horizontal Pod Autoscaler (AHPA), which utilizes RL with a Deep Q-Network (DQN) to dynamically adjust the number of Kubernetes Pods for horizontal scaling, enabling both scaling in and scaling out. We evaluate the performance and reliability of AHPA in image classification tasks, comparing its effectiveness against a traditional horizontal autoscaler in Kubernetes.

## Project Components

This project consists of the following three components, distributed across different repositories, working together seamlessly.

- [**RL-Based Autoscaler**](https://github.com/natnicha/master-thesis-auto-scaler): The main repository for RL-based Adaptive Horizontal Autoscaler (AHPA), implemented by Deep Q-Networks (DQN). It includes an agent and its learning procedure, with an ADAM optimizer set as the default.
- [**Docker-Manipulation-API**](https://github.com/natnicha/master-thesis-docker-manipulation-API): The service facilitates an RL agent by enabling seamless communication between the RL agent and the service running on Kubernetes as part of our research.
- [**Image-Classification**](https://github.com/natnicha/master-thesis-image-classification): The target application in our study, image classification, serves image classification application based on user-submitted photos.

## Built With

[<img src="https://www.python.org/static/img/python-logo.png" height="50">](https://www.python.org/) [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/PyTorch_logo_black.svg/2560px-PyTorch_logo_black.svg.png" height="50">](https://pytorch.org/) [<img src="https://flask.palletsprojects.com/en/stable/_images/flask-horizontal.png" height="50">](https://flask.palletsprojects.com/en/stable/)

<img src="https://img.shields.io/badge/Test-Pass-green"> <img src="https://img.shields.io/badge/Secuiry-Pass-blue">


## Getting Started
To start and test the service, follow the below instruction.

### Setting Up The Environment
1. Installing Python and Dependencies
This repository is developed by Python. So, install [Python](https://www.python.org/) in your working environment.

2. Our repository applies virtual environment development, [Pipenv](https://pipenv.pypa.io/en/latest/). By using this, you can simply install pipenv and create your working environment. Then install all dependencies using `pipenv install` or `pipenv sync`.

## Routes Information
Using [Flask](https://flask.palletsprojects.com/en/stable/), these following APIs are implemented.

1. **GET /**: This API is a default route for health checks, which simply returns a `hello-world` message.
2. **POST /classify**: This API serves an image classification service based on user-submitted photos.

### Starting the service
To run this service, simply run the service by flask using the following command.
```
flask run -p 30030
```

### Testing
You can simply test if your service is running success fully by opening a browser with the following website [http://localhost:30030/](http://localhost:30030/). If the service is running, you should see `Hello, World!` in the browser.


For further testing the service, use your prefer choices of API testing platforms, for example, [Postman](https://www.postman.com/). Then, use the above information for routes to make requests, for example, POST [http://localhost:30030/api/v1/ml/classify](http://localhost:30030/api/v1/ml/classify).


## Utility Commands
This section outlines a set of essential commands to help you effectively work with the project. These commands include instructions for building Docker images using Docker Compose and YML configuration files, verifying the status of the deployed application, troubleshooting common issues, and managing the overall environment. Whether you're setting up the project, ensuring the application is running properly, or performing routine maintenance, this guide offers the necessary tools to streamline the process.

### Build docker image from docker-compose.yml
```console
docker compose build

docker:desktop-linux
 => [app internal] load build definition from Dockerfile
 => [app internal] load metadata for docker.io/bitnami/pytorch:latest
 => [app auth] bitnami/pytorch:pull token for registry-1.docker.io
 => [app internal] load .dockerignore
 => => transferring context: 2B
 => [app 1/8] FROM docker.io/bitnami/pytorch:latest@sha256:f5bfd3f141efa2d9d3214c1a6d47c274430803f6030cb47d322dc909aa387ac6
 => [app internal] load build context
 => => transferring context: 831B
 => CACHED [app 2/8] ADD ./.cache ./.cache
 => CACHED [app 4/8] COPY ./app ./app
 => CACHED [app 5/8] COPY requirements.txt requirements.txt
 => CACHED [app 6/8] COPY main.py main.py
 => CACHED [app 7/8] RUN pip install -r requirements.txt
 => [app] exporting to image
 => => exporting layers
 => => writing image sha256:468df6097e58ab986fe60409cc9eafaa1d27a4e6d773621eb5fc77a0e4b6cd5b
 => => naming to 127.0.0.1:5000/master-thesis-image-recognition-app
```


### Check docker service stats 
To check its status with  `docker service ls`
```console
docker service ls
```
```console
ID            NAME      REPLICAS  IMAGE
l7791tpuwkco  registry  1/1       registry:2@sha256:1152291c7f93a4ea2ddc95e46d142c31e743b6dd70e194af9e6ebe530f782c17
```

### Start docker application
This builds the web app image, pulls an image if you don't already have it, and creates containers as described in `compose.yml`.
```console
docker compose up -d

WARNING: The Docker Engine you're using is running in swarm mode.

Compose does not use swarm mode to deploy services to multiple nodes in
a swarm. All containers are scheduled on the current node.

To deploy your application across the swarm, use `docker stack deploy`.

Creating network "ml_default" with the default driver
Building web
...(build output)...
Creating ml_redis_1
Creating ml_web_1
```


### Check docker process
To check that the app is running with `docker compose ps`:

```console
docker compose ps

      Name                     Command               State           Ports
-----------------------------------------------------------------------------------
ml_redis_1   docker-entrypoint.sh redis ...   Up      6379/tcp
ml_web_1     python app.py                    Up      0.0.0.0:8000->8000/tcp
```


### Bring the app down:
```console
docker compose down --volumes

Stopping ml_web_1 ... done
Stopping ml_redis_1 ... done
Removing ml_web_1 ... done
Removing ml_redis_1 ... done
Removing network ml_default
```

## Contributing
If you have any suggestion that would make our website looks better or more convenience, please fork the repo and create a merge requeste. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thank you again!

1. Fork the Project
2. Create your Feature Branch
    ```
    git checkout -b feature/AwesomeFeature
    ```
3. Commit your Changes
    ```
    git commit -m 'Add some AwesomeFeature'
    ```
4. Push to the Branch
    ```
    git push origin feature/AwesomeFeature
    ```
5. Open a Pull Request

## Acknowledgment
The authors would like to express our sincere gratitude to Dr. habil. Julien Vitay, thesis supervisor from the professorship of Artificial Intelligence (Informatik) at Technische Universitat at Chemnitz, for his expert guidance, unwavering support, and valuable feedback throughout the research and writing process.

We also wish to express our heartfelt appreciation to M.Sc. Florian Zimmer, our research mentor and project advisor from [Fraunhofer-Institut fur Software- und Systemtechnik (ISST)](https://www.isst.fraunhofer.de/). His generous investment of time and effort in providing regular, detailed feedback at every stage of the project was invaluable. Additionally, his insightful advice and guidance were crucial in helping us navigate and overcome the challenges encountered throughout this study. 

Importantly, we would like to gratefully acknowledge the computing time made available to them on the high-performance computer Barnard and Alpha at the, Nationales Hochleistungsrechnen, NHR Center, at Zentrum f¨ur Informationsdienste und Hochleistungsrechnen (ZIH), at Technische Universit¨at Dresden. This center is jointly supported by the Federal Ministry of Education and Research and the state governments participating in the [NHR](www.nhr-verein.de/unsere-partner).

Additionally, the following is a resource list which is helpful and would like to give credit to.

- Animal dataset: [Sharansmenon-Animals 151](https://www.kaggle.com/datasets/sharansmenon/animals141)
- Docker: [Docker](https://docs.docker.com/)


## Project Contributor & Support
This project is exclusively contributed by Natnicha Rodtong. For inquiries, feel free to contact me via [ResearchGate](https://www.researchgate.net/profile/Natnicha-Rodtong) or [email](nat.rodtong@gmail.com).

## Disclaimer
This repository is a component of a master's thesis titled `Adaptive Horizontal Pod Autoscaling (AHPA) Based on Reinforcement Learning in Kubernetes for Machine Learning`. The thesis explores advanced techniques for improving the scalability and efficiency of machine learning workloads in Kubernetes environments using reinforcement learning-based approaches for adaptive horizontal pod autoscaling. The research was conducted at [Laboratory of Artificial Intelligence, Technische Universität Chemnitz (TU Chemnitz)](https://www.tu-chemnitz.de/informatik/KI/index.php.en), Germany, as part of the requirements for completing the Master’s program. 

### Important Notes:
1. No Warranty: This project is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, or non-infringement.
2. Limitation of Liability: The authors or contributors shall not be held liable for any claim, damages, or other liability arising from the use, misuse, or inability to use the content within this repository.
3. Third-Party Dependencies: This repository may rely on external libraries or tools that are subject to their own licenses. Please ensure compliance with those licenses when using this project.
