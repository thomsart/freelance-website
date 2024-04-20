# !/usr/bin/env python3
# coding: utf-8

""" 
This module is use to execute the server of the site www.thomsart.tech
"""

import os
import smtplib, ssl
import json
import datetime

from bottle import Bottle, route, static_file, template, run, get, post, request, response, redirect

from credentials import from_email_address, from_email_password, to_email
from tools import load_file, load_feedbacks, add_feedback, is_valid_form


app = Bottle()


@app.route('/<filename>')
def return_static(filename: str):
    """ Path to return static files """

    return static_file(filename, root=load_file(filename).split(filename)[0])


@app.route('/')
def home():
    """ The path to return the home template """

    return template(load_file('home.html'), name=home)


@app.route('/contact', method='GET')
def contact():
    """  """

    return template(load_file('contact.html'), name=contact)


@app.route('/contact', method='POST')
def contact():
    """
    This view retrieves all datas from contact form
    """

    email = str(request.forms.getunicode('email'))
    job = str(request.forms.getunicode('job'))
    link = str(request.forms.getunicode('link'))

    if is_valid_form(email=email, job=job, link=link):

        msg = f"""\n
            From: {email}\n
            Job: {job}\n
            Link: {link}"""

        msg = bytes(msg, 'utf-8')
        # on rentre les renseignements pris sur le site du fournisseur
        smtp_address = 'smtp.gmail.com'
        smtp_port = 465

        try:
            # on crée la connexion
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
                # connexion au compte
                server.login(from_email_address, from_email_password)
                # envoi du mail
                server.sendmail(email, to_email, msg)

                return redirect('/') 

        except:
            return template(load_file('error_mail.html'))

    else:
        return template(load_file('error_mail.html'))


@app.route('/blog', method='GET')
def blog():
    """  """

    with open(load_file("feedbacks.json"), "r", encoding="utf-8") as file:
        dict_file = json.load(file)

    feedbacks = sorted(dict_file.items(), key=lambda x: x[0], reverse=True)

    return template(load_file("blog.html"), feedbacks=feedbacks)


@app.route('/comment', method="GET")
def comment():
    """  """

    return template(load_file("comment.html"), name=comment)


@app.route('/comment', method="POST")
def comment():
    """  """

    datas = {
        "name": str(request.forms.getunicode('name')),
        "company": str(request.forms.getunicode('company')),
        "comment": str(request.forms.getunicode('comment')),
        "link": str(request.forms.getunicode('link'))
    }

    today = str(datetime.date.today())

    copy = load_feedbacks()

    if today in copy:
        copy[today].append(datas)
    else:
        copy[today] = [datas]
        print(copy)

    if add_feedback(copy):

        return redirect('/blog')

    else:

        return template(load_file("error_comment.html"), name=comment)


@app.route('/mentions_legales')
def mentions_legales():
    """ The path to return the mentions legales template """

    return template(load_file("mentions_legales.html"), name=mentions_legales)



if __name__ == '__main__':
    print('launch on local')
    run(app, host='localhost', port=8080, debug=True, reloader=True)
else:
    print('launch on vps')
    app.run(server='gunicorn')
