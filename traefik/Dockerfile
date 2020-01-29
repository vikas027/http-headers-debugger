FROM traefik:1.7.20-alpine

LABEL maintainer=vikas@reachvikas.com

# Not required, just added for troubleshooting
RUN apk add --no-cache curl && \
    rm -rf /tmp/* /var/cache/apk/* /var/tmp/*

COPY traefik.toml /etc/traefik/traefik.toml
