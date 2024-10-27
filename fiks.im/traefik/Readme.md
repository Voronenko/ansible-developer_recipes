# Short notes

to run `docker-compose up -d`

once executed, on  http://traefik.lvh.voronenko.net:8880/  you can find dashboard.

Take a look on example of

http://whoami.lvh.voronenko.net:880
and
https://whoami.lvh.voronenko.net:8443


Traefik serves only containers that share `traefik-public` docker network.

That introduces some isolation to the application into "public" and "private" parts when needed

for ideas to enable your service as https and http


# Integrating external services 


```yaml

version: '3.4'
services:
  whoami2:
    image: "containous/whoami"
#    container_name: "simple-service2"
    networks:
      - traefik-public
    labels:
      - "traefik.enable=true"
#      - "traefik.http.middlewares.whoami2-https.redirectscheme.scheme=https"
      - "traefik.http.routers.whoami2-http.entrypoints=web"
      - "traefik.http.routers.whoami2-http.rule=Host(`whoami2.lvh.voronenko.net`)"
#      - "traefik.http.routers.whoami2-http.middlewares=whoami2-https@docker"
      - "traefik.http.routers.whoami2.entrypoints=websecure"
      - "traefik.http.routers.whoami2.rule=Host(`whoami2.lvh.voronenko.net`)"
      - "traefik.http.routers.whoami2.tls=true"
      - "traefik.http.routers.whoami2.tls.certresolver=default"
networks:
  traefik-public:
    external: true
```


# Configuration via files and commandline

2BD

```
[log]
  level = "ERROR"

[providers.docker]
  exposedByDefault = false
  endpoint = "tcp://dockerproxy:2375"
  network = "traefik"

[api]
  dashboard = true
  debug = true

[entryPoints]
  [entryPoints.web]
    address = ":80"
  [entryPoints.web-secure]
    address = ":443"
  [entryPoints.dashboard]
    address = ":8080"

[certificatesResolvers]
  [certificatesResolvers.default.acme]
    email = "contact@myemail.com"
    storage = "acme.json"
    [certificatesResolvers.default.acme.tlsChallenge]
```


