FROM alpine:3.7

LABEL maintainer=vikas@reachvikas.com

RUN apk add --no-cache python && \
    rm -rf /tmp/* /var/cache/apk/* /var/tmp/*

COPY server.py /server.py

ENTRYPOINT ["/server.py"]
