# services/Makefile

build_server:
	docker-compose up --build

test_api:
	docker-compose exec api pytest "src/tests" -p no:warnings --cov="src"
