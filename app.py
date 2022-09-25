import datetime
from flask import Flask, request, render_template, redirect, flash, session, jsonify, url_for
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_uploads import configure_uploads, IMAGES, UploadSet
# from forms import User_registration, Create_memorial_form, Post_form, LoginForm, ZipForm, AddFlowerToCart, FlowerOrderForm
import json 
from models import db, connect_db, Msg, User
from os import getenv
# import requests, base64
# import socket
# from flowershop import *
import pdb
# from date_and_time_functions import *

# from CRUD_psql import * 

#TODO: TEMPORARY - ***** move these to environment variables and put in heroku *****
from secrets import API_SECRET_KEY

# ****NEED TO ALSO INSTALL Flask-Reloaded in requirements TO FIX BUGS IN flask_uploads!!!

#TODO:
# from forms import User_registration, User_login, Admin_registration, Admin_login

app=Flask(__name__)


# original local postgresql db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///comicswap2'

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

app.config['SECRET_KEY'] = API_SECRET_KEY

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)

connect_db(app)


# app.config['UPLOADED_IMAGES_DEST'] = 'static/images'

# images = UploadSet('images', IMAGES)
# configure_uploads(app, images)


# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


WTF_CSRF_SECRET_KEY = 'magic'



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


################################### LOGIN/REGISTER ####################################

@app.route('/login', methods=["GET"])
def login():
    """ login page - should have a form, check the data, and pass along - use sessions to maintain login for ___ hours..."""

    return render_template("login.html")

@app.route('/register', methods=["GET"])
def register():
    """ register page - should have a form, check the data, and pass along - use sessions to maintain login for ___ hours..."""

 
    return render_template("register.html")


################################################################################

@app.route('/myaccount', methods=["GET"])
def myaccount():
    """ My Account page - should have CRUD functionality for personal info, preferences, credit card on file, etc...."""

    return render_template("myaccount.html")


@app.route('/about', methods=["GET"])
def about():
    """ about page - should tell about company and benefits"""

    return render_template("about.html")



@app.route('/mystuff', methods=["GET"])
def mystuff():
    """ My Stuff page - should have link to user's library of trade offerings, list of offers made, offers received, things being shipped, books that they are watching for..."""

    return render_template("mystuff.html")



@app.route('/comicdetail', methods=["GET"])
def comicdetail():
    """ Comic Detail page - should have links to a specific user's comic with all details and option to edit it"""

    return render_template("comic-detail.html")



@app.route('/search', methods=["GET"])
def search():
    """ Search page - should default to most popular titles available, and be able to search books by title, date range, pedigree, condition, price range..."""
 
    return render_template("search.html")



###############################  MAIL ROUTES #################################

@app.route('/messages', methods=["GET"])
def inbox():
    """ inbox page - should show all messages recieved from members with a mail search box and pagination"""
 
    return render_template("messages.html")


@app.route('/msgsent')
def msgsent():
    """ alerts that a  messages was sent from user 
    TODO: create message and send alert to receiver
    """

    # msg = Message()
    # message = msg.create(3, " Bob Ross", "this is a test msg", "this is a message just a message of some size to try things out", "attachment details", False)

    flash(f'WHERE WE CREATE A NEW MSG THROUGH SQLAlchemy!')

 
    return redirect("/messages")


@app.route('/sent', methods=["GET"])
def sent():
    """ sent comicswap mail page - should show a list of all messages sent from user with pagination and clickable to maildetail and have a reply and delete button"""
 
    return render_template("sent.html")


@app.route('/drafts', methods=["GET"])
def drafts():
    """ sent comicswap mail page - should show all messages sent between members with pagination with save and send buttons"""
 
    return render_template("drafts.html")


@app.route('/maildetail', methods=["GET"])
def maildetail():
    """ single comicswap email page - should show single message sent between members for closer reading and include a reply button and a delete button (possibly forward?) """
 
    return render_template("maildetail.html")


@app.route('/newmail', methods=["GET"])
def newmail():
    """ write an email page - should show form to create an e-mail and send"""
 
    return render_template("newmail.html")

@app.route('/deletemsg', methods=["GET"])
def deletemsg():
    """ write an email page - should show form to create an e-mail and send"""
 
    return render_template("deletemsg.html")


########################### MAILING LIST ###########################################

@app.route('/subscribe', methods=["GET"])
def subscribe():
    """ write an email page - should show form to create an e-mail and send"""
 
    return render_template("subscribe.html")

########################### TRADING ###########################################

@app.route('/offertrade', methods=["GET"])
def offertrade():
    """ processes the request for a trade.  Should:
    - send a message to book owner asking for it and the terms including additional money if app.
    - Shows message saying "this constitutes a binding contract and if the trade is canceled by either party the fee will still be owed (?)
    """
 
    return render_template("offertrade.html")

@app.route('/acceptoffer', methods=["GET"])
def acceptoffer():
    """ processes the acceptance of a trade offer.  Should:
    - acknowledge the trade onscreen
    - inform offerrer
    - charge offerrer's card
    - send information via message and email to offerrer and accepter on how to mail items
    - update status of that comic and trade so it shows trade status in my stuff
    """

    return render_template("acceptoffer.html")


# TODO: FINISH THIS ONE...
@app.route('/markedasmailed', methods=["GET"])
def markedasmailed():
    """ 
    - possibly change this to an update tradestatus() function and pass in the marked as mailed
    - get here from my stuff trades list and/or trade detail page on a comic
    - offer ability to change it to accepted/not mailed, mailed/en route to TheComicSwap, received by TheComicSwap/being inspected, inspection approved/not mailed, inspected/passed/en route to reciver, received by reciever/$ not released, transaction successful/$ released
    
    """
 
    return render_template("markedasmailed.html")
