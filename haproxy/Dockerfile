FROM haproxy:1.8.4-alpine

LABEL maintainer=vikas@reachvikas.com

# Not required, just added for troubleshooting
RUN apk add --no-cache curl && \
    rm -rf /tmp/* /var/cache/apk/* /var/tmp/*

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
