FROM quay.io/pixie79/python_webapp
MAINTAINER pixie79

RUN pip install flask-bootstrap
CMD mkdir /app
ADD app.wsgi /app/app.wsgi
CMD service apache2 start && tail -F /var/log/apache2/err.log
EXPOSE 5000
