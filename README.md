# Flask RESTful API

This project is an attempt to build a boiler plate flask restful API that can be used for developing RESTful APIs quickly. As a sample, the APIs currently exposed are GET for "/" and "/status".


GET for "/" returns "Hello World"

GET for "/status" returns the following with lastcommitsha is repository's commit hash at build time

```

  "myapplication": [
    {
      "version": "1.0",
      "description": "pre-interview technical test",
      "lastcommitsha": "abc57858585"
    }
  ]
}
```

The project also includes a travis pipeline described in .travis.yml with two stages:
* test - Runs unittest
* build - Builds the docker image and pushes to dockerhub
 
The lastshacommit information is created only when deployed and run via docker. So if you are running the endpoint locally without docker and hitting the /status endpoint, you will see an "Internal Server Error" which is expected. 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

#### Operating system
* Mac OSX
* Linux

#### Software 
* Docker
* Python 2.7 (For running unittests and any further development)

### Installing

Get the image from docker

```
docker pull ansri1980/boiler_plate_rest
```

Run the docker image

```
docker run -d -p 5000:5000 ansri1980/boiler_plate_rest:latest
```

Check if the docker container is up and running

```
docker ps
```

If the container is successfully started, you should see something like

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
d953d49c6407        1af50af07d32        "python boiler_plate…"   About an hour ago   Up About an hour    0.0.0.0:5000->5000/tcp   stupefied_lewin
```

You can do a simple test

```
$ curl http://127.0.0.1:5000
"Hello World"


$curl http://127.0.0.1:5000/status
{"myapplication":[{"description":"pre-interview technical test","lastcommitsha":"634042d7f9100a05c3aa032e02e18dea84e59549","version":"1.0"}]}
```

## Development and Unittesting

Clone the repo

```
https://github.com/ansri1980/bug-free-pancake.git
```

Install the python requirements

``` 
cd bug-free-pancake/app
pip install -r requirements.txt
```

To run unittests

```
python -m unittest tests.test_boiler_plate
```

To run the application locally on your machine do the following. But make sure that the default port 5000 is free to use. If you are running the docker application, please stop the same before running the application locally.  

```
python boiler_plate_rest_api.py
 * Serving Flask app "boiler_plate_rest_api" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Now you can hit the endpoint via your browser or via curl as mentioned earlier

For unittest, unittest.Testcase is used in this code although pytest is recommended. 

## Deployment

Deployment is out of scope for this project, although I would recommend ECS in AWS. 

## Authors

* **Anand Sridharan** - *Initial work* - [ansri1980](https://github.com/ansri1980)


## License

Feel free to clone it and experiment. 

## Acknowledgments

* https://docs.travis-ci.com
* https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5

