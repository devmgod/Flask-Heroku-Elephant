import datetime
from flask import Flask, request, render_template, redirect, flash, session, jsonify, url_for
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_uploads import configure_uploads, IMAGES, UploadSet
# from forms import User_registration, Create_memorial_form, Post_form, LoginForm, ZipForm, AddFlowerToCart, FlowerOrderForm
import json 
# from models import db, connect_db, User, Admin_user, Departed, Post, Order, Order_item
from os import getenv
import requests, base64
import socket
# from flowershop import *
import pdb
# from date_and_time_functions import *

from StrapiCRUD import Articles    

#TODO: TEMPORARY - ***** move these to environment variables and put in heroku *****
# from secrets import API_SECRET_KEY

# ****NEED TO ALSO INSTALL Flask-Reloaded in requirements TO FIX BUGS IN flask_uploads!!!

#TODO:
# from forms import User_registration, User_login, Admin_registration, Admin_login

app=Flask(__name__)

# original local postgresql db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///remembertogether'

#secure variables
#At ElephantSQL
# app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQL_CONNECTION_STRING', 'postgresql:///remembertogether') #2nd is the backup source
# app.config['SECRET_KEY']= getenv('API_SECRET_KEY')

# IN ACTUAL HEROKU DEPLOYMENT THIS IS A SEPARATE ENVIRONMENT VARIABLE!
# app.config['SECRET_KEY']= API_SECRET_KEY
# app.config['API_SECRET_KEY']=getenv('API_SECRET_KEY')

# app.config['FLORIST_ONE_KEY']= getenv('FLORIST_ONE_KEY')
# app.config['FLORIST_ONE_PASSWORD']= getenv('FLORIST_ONE_PASSWORD')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# app.config['UPLOADED_IMAGES_DEST'] = 'static/images'

# images = UploadSet('images', IMAGES)
# configure_uploads(app, images)


# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# debug = DebugToolbarExtension(app)

# WTF_CSRF_SECRET_KEY = 'magic'



strapi_url = "http://localhost:1337/api"

# @app.route("/http://localhost:1337/api/articles?populate=*", methods=["GET"])
# def getArticles():
#     """ routing properly (hopefully) to get all articles from STRAPI"""
#     data = request.json
#     return render_template("index.html", articles=data)

# def request_article(issue):
#     url = strapi_url + "/articles?populate=*"
#     response = requests.get(url)
#     r = response.json()
#     # articles = json.loads(r)


#     title1=articles['data'][issue]['attributes']['title']

#     return {'title1':title1}



@app.route('/', methods=["GET"])
def home():
    """ home page - should give login option and information about app"""

    return render_template("index.html")


@app.route('/login', methods=["GET"])
def login():
    """ login page - should have a form, check the data, and pass along - use sessions to maintain login for ___ hours..."""

    return render_template("login.html")

@app.route('/register', methods=["GET"])
def register():
    """ register page - should have a form, check the data, and pass along - use sessions to maintain login for ___ hours..."""

 
    return render_template("register.html")

@app.route('/myaccount', methods=["GET"])
def myaccount():
    """ My Account page - should have CRUD functionality for personal info, preferences, credit card on file, etc...."""

 
    return render_template("myaccount.html")

@app.route('/about', methods=["GET"])
def about():
    """ about page - should tell about company and benefits"""

 
    return render_template("about.html")

@app.route('/messages', methods=["GET"])
def messages():
    """ messages page - should have full CRUD internal messaging capability"""

 
    return render_template("messages.html")

@app.route('/mystuff', methods=["GET"])
def mystuff():
    """ My Stuff page - should have link to user's library of trade offerings, list of offers made, offers received, things being shipped, books that they are watching for..."""

 
    return render_template("mystuff.html")

@app.route('/search', methods=["GET"])
def search():
    """ Search page - should default to most popular titles available, and be able to search books by title, date range, pedigree, condition, price range..."""

 
    return render_template("search.html")

