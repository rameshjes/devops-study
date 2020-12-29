docker run --rm -it -v /home/ramesh/github/german:/home/german -v `pwd`:/home/app learn-devops bash

# enter into docker and mount repos directory (so that changes in docker can reflect for comimit)
docker run --rm -it -v `pwd`:/home/app learn-devops bash