# data-engineer-challenge
Challenge Data Engineer


- Install Docker Desktop on Windows, it will install Docker Compose as well, Docker Compose will allow you to run multiple container applications.
- Install git-bash for windows, once installed, open git bash and download this repository, this will download the docker-compose.yaml file, and other files needed.

ramse@DESKTOP-K6K6E5A MINGW64 /c
$ git clone https://github.com/Wittline/data-engineer-challenge.git
Once all the files needed were downloaded from the repository, let's run everything. We will use the git bash tool again, go to the folder data-engineer-challenge and we will run the Docker Compose command:

ramse@DESKTOP-K6K6E5A MINGW64 /c
$ cd data-engineer-challenge
ramse@DESKTOP-K6K6E5A MINGW64 /c/data-engineer-challenge
$ cd code
ramse@DESKTOP-K6K6E5A MINGW64 /c/data-engineer-challenge/code
$ cd apps
@DESKTOP-K6K6E5A MINGW64 /c/data-engineer-challenge/code/apps
$ docker-compose up
After wait for a couple of minutes the final result of executing the above command should look like this:
docker-compose executionlet's check the API REST, go to your browser and search for: http://localhost:8080/docs#/default

let's try the request to the API REST

let's check the response from the API REST
