""" !/usr/bin/env python3
    -*- coding: utf-8 -*-

This module is use to execute the server of the site www.thomsart.tech """

import smtplib, ssl
import json

from bottle import Bottle, route, static_file, template, run, get, post, request

from const import *
from credentials import *



app = Bottle()

@app.route('/<filename>')
def return_static(filename: str):
    """ All paths to return static files """

    if str(filename) in css:
        return static_file(filename, root=css_root)

    elif str(filename) in js:
        return static_file(filename, root=js_root)

    elif str(filename) in font_title:
        return static_file(filename, root=font_title_root)
    
    elif str(filename) in font_text:
        return static_file(filename, root=font_text_root)

    elif str(filename) in icon:
        return static_file(filename, root=icon_root)

    elif str(filename) in photo:
        return static_file(filename, root=photo_root)

    else:
        print(f"This file {filename} is unknow...")

@app.route('/')
def home():
    """ The path to return the home template """

    return template('home', name=home)


@app.route('/contact', method='GET')
def contact():
    """  """

    return template('contact', name=contact)


@app.route('/contact', method='POST')
def contact():
    """  """

    client_email = request.forms.get('email')
    job = request.forms.get('job')
    link = request.forms.get('link')

    msg = f"""\n
        From: {client_email}\n
        Job:  {job}\n
        Link: {link}"""

    # on rentre les renseignements pris sur le site du fournisseur
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465
    # on crée la connexion
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        # connexion au compte
        server.login(from_email_address, from_email_password)
        # envoi du mail
        server.sendmail(client_email, to_email, msg)

    return template('home', name=contact)


@app.route('/blog')
def blog():
    """  """

    return template('blog', name=blog)


@app.route('/mentions_legales')
def mentions_legales():
    """ The path to return the mentions legales template """

    return template('mentions_legales', name=mentions_legales)



if __name__ == '__main__':
    print('launch on local')
    run(app, host='localhost', port=8080, debug=True, reloader=True)
else:
    print('launch on vps')
    app.run(server='gunicorn')
