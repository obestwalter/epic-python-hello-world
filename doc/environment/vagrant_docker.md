# Vagrant vs Docker

There is actually no vs - Vagrant has it covered:

http://www.vagrantup.com/blog/feature-preview-vagrant-1-6-docker-dev-environments.html

http://phusion.github.io/baseimage-docker/

Vagrant is for managing portable development environments, Docker is for building and running application environments.

Pro Vagrant: http://stackoverflow.com/a/21314566/2626627

Pro Docker: http://stackoverflow.com/a/22370529/2626627


# Vagrant

# Vagrant with Windows host

https://eamann.com/tech/vagrant-windows/


# Docker

## Articles

https://serversforhackers.com/articles/2014/03/20/getting-started-with-docker/
https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications

## Tutum private registry

http://us8.campaign-archive1.com/?u=57b9190b37cc6cc0a3cf93b0a&id=071cfad63a&e=5dbe5c95e7

## Setup after installation

### Control docker as non root 

http://askubuntu.com/a/477554/266253

### add completion for your shell

* bash: https://github.com/docker/docker/blob/master/contrib/completion/bash/docker
* zsh: https://github.com/felixr/docker-zsh-completion

## Deployment on AWS

https://support.tutum.co

## Automate with Dockerfile

http://docs.docker.com/reference/builder/

## Mount/Map directories into docker: http://docs.docker.com/userguide/dockervolumes/

## Misc

## python docker image: https://registry.hub.docker.com/_/python/
* autogenerate dockerfile from ubuntu image http://kracekumar.com/post/70198562577/autogenerate-dockerfile-from-ubuntu-image
* Using docker to run python https://civisanalytics.com/blog/engineering/2014/08/14/Using-Docker-to-Run-Python/

### Tidy up all local stuff (after experiments)

    #!/bin/bash
    # Delete all containers
    docker rm $(docker ps -a -q)
    # Delete all images
    docker rmi $(docker images -q)
    


## Technical details

https://docs.docker.com/terms/image/#base-image-def
https://docs.docker.com/reference/builder/
https://docs.docker.com/articles/dockerfile_best-practices/

## Advanced

* smallest possible container: http://blog.xebia.com/2014/07/04/create-the-smallest-possible-docker-container/


## Windows

Docker: http://docs.docker.com/installation/windows/
