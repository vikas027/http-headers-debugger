# http-headers-debugger
Debug HTTP headers with docker containers

# Tools Used

- OS X 10.15.2 as a Docker Host (should not matter)
- Docker v19.03.5
- Docker Compose v1.25.2
- Nginx v1.17.8
- Traefik v1.7.20
- HAProxy v1.6.15

# Build and start the containers

```bash
$ docker-compose up --build -d
$ docker logs -f debugheaders (optional)
```

# From a new terminal

- Check Nginx

```bash
$ curl -H 'Accept: application/json' -H 'something: random' http://localhost:8081
connection: close
accept: application/json
user-agent: curl/7.68.0
host: localhost:8081
x-forwarded-proto: http
something: random
x-forwarded-server: localhost

HTTP/1.0 200
Server: SimpleHTTP/0.6 Python/2.7.16
Date: Wed, 29 Jan 2020 10:17:28 GMT
curl: (18) transfer closed with 485 bytes remaining to read
```

- Check Traefik

```bash
$ curl -H 'Host: debugheaders.docker.local' http://localhost:8080
accept-encoding: gzip
x-forwarded-host: debugheaders.docker.local
x-forwarded-port: 80
x-forwarded-for: 172.21.0.1
accept: */*
user-agent: curl/7.68.0
host: debugheaders.docker.local
x-forwarded-proto: http
x-real-ip: 172.21.0.1
x-forwarded-server: 1ceaa33bade2

HTTP/1.0 200
Server: SimpleHTTP/0.6 Python/2.7.16
Date: Wed, 29 Jan 2020 10:18:10 GMT
curl: (18) transfer closed with 380 bytes remaining to read
```

- Check HAProxy

```bash
$ curl -H 'Accept: application/json' -H 'Content-Type: application_json' http://localhost:8082
x-forwarded-for: 172.21.0.1
connection: close
accept: application/json
user-agent: curl/7.68.0
host: localhost:8082
x-forwarded-proto: http
content-type: application_json

HTTP/1.0 200
Server: SimpleHTTP/0.6 Python/2.7.16
Date: Wed, 29 Jan 2020 10:18:33 GMT
curl: (18) transfer closed with 474 bytes remaining to read
```
