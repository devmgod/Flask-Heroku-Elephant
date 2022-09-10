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

# @app.route('/')
# def home():
#     """ home page - should give login option and information about app"""
    
#     departed = Departed.query.all()
#     return render_template("index.html", departed=departed)

strapi_url = "http://localhost:1337/api"

@app.route('/', methods=["GET"])
def home():
    """ home page - should give login option and information about app"""

    # articles = Articles()
    # print(articles.all())

    articles = requests.get(strapi_url + "/articles?populate=*")

    return render_template("index.html", articles=articles)

