# Data Engineer Challenge

This goal of this repository is based on solving a technical challenge for the data engineering position.

Check the article here:  <a href="https://coraspe-ramses.medium.com/design-development-and-deployment-of-a-simple-data-pipeline-6f1d59d0fd6a/">Design, Development and Deployment of a simple Data Pipeline</a>


![image](https://user-images.githubusercontent.com/8701464/172062180-c90e7f11-ae64-4fd2-9772-8cfd2fb6abf6.png)


- Install Docker Desktop on Windows, it will install Docker Compose as well, Docker Compose will allow you to run multiple container applications.
- Install git-bash for windows, once installed, open git bash and download this repository, this will download the docker-compose.yaml file, and other files needed.


```linux 
ramse@DESKTOP-K6K6E5A MINGW64 /c
$ git clone https://github.com/Wittline/data-engineer-challenge.git
```

- Once all the files needed were downloaded from the repository, let's run everything. We will use the git bash tool again, go to the folder data-engineer-challenge and we will run the Docker Compose command:

```linux 
ramse@DESKTOP-K6K6E5A MINGW64 /c
$ cd data-engineer-challenge
```

```linux 
ramse@DESKTOP-K6K6E5A MINGW64 /c/data-engineer-challenge
$ cd code
```
```linux 
ramse@DESKTOP-K6K6E5A MINGW64 /c/data-engineer-challenge/code
$ cd apps
```

```linux 
@DESKTOP-K6K6E5A MINGW64 /c/data-engineer-challenge/code/apps
$ docker-compose up
```

- After wait for a couple of minutes the final result of executing the above command should look like this:

![image](https://user-images.githubusercontent.com/8701464/172062212-05193fba-d980-4917-9fe1-f1134d72afb8.png)


- docker-compose executionlet's check the API REST, go to your browser and search for: http://localhost:8080/docs#/default

![image](https://user-images.githubusercontent.com/8701464/172062217-9fbd6026-6a49-42fc-bbbb-9efb58743cc9.png)


- let's try the request to the API REST

![image](https://user-images.githubusercontent.com/8701464/172062224-b9ec90bd-8454-4e5a-a4f5-2adc932a41a2.png)


- let's check the response from the API REST

![image](https://user-images.githubusercontent.com/8701464/172062241-8fc66570-9ca8-4ff9-b56e-239fb6eee118.png)

# Contributing and Feedback
Any ideas or feedback about this repository?. Help me to improve it.

# Authors
- Created by <a href="https://twitter.com/RamsesCoraspe"><strong>Ramses Alexander Coraspe Valdez</strong></a>
- Created on 2022

# License
This project is licensed under the terms of the Apache License.


