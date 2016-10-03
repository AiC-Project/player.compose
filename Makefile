
clean: ;

docker-images:
	docker-compose -f build-project.yml build
	docker-compose -f build-player.yml build

project-up:
	docker-compose -f run-project.yml up --no-build -d

project-down:
	docker-compose -f run-project.yml down -v

player-up:
	docker-compose -f run-player.yml up --no-build

player-down:
	docker-compose -f run-player.yml down -v

