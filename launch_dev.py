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
from tools import return_file_path, load_feedbacks, add_feedback, is_valid_form
from const import URLS

app = Bottle()


@app.route(URLS['home'], method="GET", name='home')
def home():
    """
    View for home.
    """

    return template(return_file_path('home.html'))


@app.route(URLS['contact'], method="GET", name="contact")
def contact():
    """
    View to get the contact form.
    """

    return template(return_file_path('contact.html'))


@app.route(URLS['contact'], method="POST",name="contact")
def contact():
    """
    View to post contact form.
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

                return redirect(URLS['home']) 
        except:
            return template(return_file_path('error_mail.html'))
    else:
        return template(return_file_path('error_mail.html'))


@app.route(URLS['blog'], method='GET', name="blog")
def blog():
    """
    View to render the blog.
    """

    with open(return_file_path("feedbacks.json"), "r", encoding="utf-8") as file:
        dict_file = json.load(file)

    feedbacks = sorted(dict_file.items(), key=lambda x: x[0], reverse=True)

    return template(return_file_path("blog.html"), feedbacks=feedbacks)


@app.route(URLS['comment'], method="GET", name='comment')
def comment():
    """
    The view to retrieve comments for the Blog.
    """

    return template(return_file_path("comment.html"))


@app.route(URLS['comment'], method="POST", name='comment')
def comment():
    """
    The view to leave a comment on the Blog.
    """

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

    if add_feedback(copy):
        return redirect(URLS['blog'])

    else:
        return template(return_file_path("error_comment.html"))


@app.route(URLS['mentions_legales'], method="GET", name='mentions_legales')
def mentions_legales():
    """
    View for the mentions legales.
    """

    return template(return_file_path("mentions_legales.html"))


@app.route(URLS['static'], method="GET")
def return_static(filename: str):
    """
    View for the static files.
    """

    return static_file(filename, root=return_file_path(filename).split(filename)[0])


if __name__ == '__main__':
    print('launch on local')
    run(app, host='localhost', port=8080, debug=True, reloader=True)
else:
    print('launch on vps')
    app.run(server='gunicorn')
