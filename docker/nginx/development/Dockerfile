FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
ADD ./docker/nginx/development/nginx.conf /etc/nginx/nginx.conf

RUN mkdir /var/www
RUN mkdir /var/www/static

WORKDIR /var/www/static
