test:
	docker run --rm -it -v `pwd`:/home/app learn-devops pytest -sxvv src/tests
lint:
	pre-commit install && pre-commit run -a -v
build:
	docker build -t "learn-devops" .
run:
	docker run --rm -it -v `pwd`:/home/app learn-devops bash