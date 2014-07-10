from app import app
from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/status')
@app.route('/ping')
def ping():
    return render_template('status.html',
                           ua=request.headers.get('User-Agent'),
                           ip=request.remote_addr,
                           ipheader=request.headers.getlist("X-Forwarded-For"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
