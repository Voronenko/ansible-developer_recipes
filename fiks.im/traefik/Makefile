create-traefik-network-once:
	docker network create --driver=overlay --attachable  traefik-public
	docker network create traefik
up:
	docker-compose up -d
down:
	docker-compose down

up-swarm:
	docker stack deploy --compose-file=docker-compose.yml traefik
down-swarm:
	docker stack rm traefik

reload:
	docker-compose restart traefik

