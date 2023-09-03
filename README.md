### Dockerized Flask Morse App. ###

This repo contains a dockerfile and an application that translates input strings to morse code.


1. build the image:

    docker build -t image/name:tag -f Dockerfile_app .

2. run a container from the image:

    docker run -d -p 5000:5000

3. now you can navigate to "http://host IP:5000/morse/value to translate" and view the app page.
