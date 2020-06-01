FROM php:7.3-apache
COPY ./phpProject/website/ /var/www/html/
EXPOSE 80
