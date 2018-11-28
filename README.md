Build the docker image as follows:
$ docker build -t base_flask_api:latest .

Check if images are created:
$ docker images

Check if docker instance is running:
$ docker ps

Run a docker instance of the image:
$ docker run -d -p 5000:5000 base_flask_api:latest

To stop a docker instance
$ docker stop [pid]

To kill a docker instance
$ docker kill [pid]

To kill by signal a docker instance
$ docker kill --signal=SIGTERM [pid]

To kill by signal all docker instances
$ docker kill --signal=SIGTERM $(ps -qa)

Open a browser:
$ open -a 'Google Chrome' http://127.0.0.1:5000/

Or, via curl
$ curl http://127.0.0.1:5000/
