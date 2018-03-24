# http-headers-debugger
Debug HTTP headers with docker containers

# Tools Used

- OS X 10.11.2 as a Docker Host (should not matter)
- Docker v17.12.0-ce
- Docker Compose v1.18.0
- Nginx v1.13.10
- Traefik v1.5.4
- HAProxy v1.8.4

# Build and start the containers

```
$ docker-compose up --build -d
$ docker logs -f debugheaders (optional)
```

# From a new terminal

- Check Nginx

```
$ curl -H 'Accept: application/json' -H 'Content-Type: application/json' http://localhost:8081
connection: close
accept: application/json
user-agent: curl/7.43.0
host: localhost:8081
x-forwarded-proto: http
x-forwarded-server: localhost
content-type: application/json

HTTP/1.0 200
Server: SimpleHTTP/0.6 Python/2.7.14
Date: Fri, 23 Mar 2018 12:39:10 GMT
curl: (18) transfer closed with 444 bytes remaining to read
```

- Check Traefik

```
$ curl -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Host: debugheaders.docker.local' http://localhost:8080
accept-encoding: gzip
x-forwarded-host: debugheaders.docker.local
x-forwarded-port: 80
x-forwarded-for: 172.18.0.1
accept: application/json
user-agent: curl/7.43.0
host: debugheaders.docker.local
x-forwarded-proto: http
x-real-ip: 172.18.0.1
x-forwarded-server: a006041875ad
content-type: application/json

HTTP/1.0 200
Server: SimpleHTTP/0.6 Python/2.7.14
Date: Fri, 23 Mar 2018 12:40:23 GMT
curl: (18) transfer closed with 307 bytes remaining to read
```

- Check HAProxy

```
$ curl -H 'Accept: application/json' -H 'Content-Type: application_json' http://localhost:8082
x-forwarded-for: 172.18.0.1
connection: close
accept: application/json
user-agent: curl/7.43.0
host: localhost:8082
x-forwarded-proto: http
content-type: application_json

HTTP/1.0 200
Server: SimpleHTTP/0.6 Python/2.7.14
Date: Fri, 23 Mar 2018 13:06:16 GMT
curl: (18) transfer closed with 446 bytes remaining to read
```
