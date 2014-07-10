FROM python_webapp
MAINTAINER pixie79

CMD mkdir /app
ADD app.wsgi /app/wsgi
CMD service apache2 start && tail -F /var/log/apache2/err.log
