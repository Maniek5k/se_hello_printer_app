.PHONY: test
.DEFAULT_GOAL := test

USERNAME=maniek5k
SERVICE_NAME=hello-world-printer
MY_DOCKER_NAME=$(SERVICE_NAME)
TAG=$(USERNAME)/$(MY_DOCKER_NAME)

deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt
lint:
	flake8 --max-line-length=120 hello_world test 
run:
	python main.py
test:
	PYTHONPATH=. py.test --verbose -s
	
test_smoke:
	curl --fail 127.0.0.1:5000
	curl -s -o /dev/null -w "%{http_code}" --fail 127.0.0.1:5000

test_cov:
	PYTHONPATH=. py.test --verbose -s --cov=.

test_xunit:
	PYTHONPATH=. py.test --verbose -s --cov=. --cov-report xml

docker_build:
	docker build -t $(MY_DOCKER_NAME) .

docker_run: docker_build
	docker run \
		--name $(SERVICE_NAME)-dev \
		-p 5000:5000 \
		-d $(MY_DOCKER_NAME)

docker_run_local:
	docker run \
		-p 5000:5000 \
		$(USERNAME)/$(SERVICE_NAME)

docker_stop_local:
	docker stop $(USERNAME)/$(SERVICE_NAME)

docker_stop:
	docker stop $(SERVICE_NAME)-dev

docker_push: docker_build
	docker login --username $(USERNAME) --password $${DOCKER_PASSWORD} docker.io; \
	docker tag $(MY_DOCKER_NAME) $(TAG); \
	docker push $(TAG); \
	docker logout;


