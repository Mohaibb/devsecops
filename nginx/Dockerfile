FROM nginx:1.27-alpine

# Remove default config
RUN rm /etc/nginx/conf.d/default.conf || true

COPY nginx.conf /etc/nginx/nginx.conf

# Ensure nginx owns its dirs (optional but good practice)
RUN chown -R nginx:nginx /var/cache/nginx /var/run /var/log/nginx /etc/nginx

# Drop privileges
USER nginx

EXPOSE 80 443
