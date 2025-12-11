FROM nginx:1.27-alpine

# Remove default config
RUN rm /etc/nginx/conf.d/default.conf || true

COPY nginx.conf /etc/nginx/nginx.conf
COPY certs /etc/nginx/certs

EXPOSE 80 443
