FROM nginx

# Remove default configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Replace configuration file with nginx.conf
COPY nginx.conf /etc/nginx/conf.d
