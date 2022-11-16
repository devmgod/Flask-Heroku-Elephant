# import datetime
from flask import Flask, request, render_template, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_uploads import configure_uploads, IMAGES, UploadSet
# import forms
# import json 
from .models import db, connect_db, Msg, User, Comic
from os import getenv
# import requests, base64
# import socket
# from flowershop import *
# import pdb

from forms import EditComicsForm, SubscriptionForm
# from date_and_time_functions import *

# from CRUD_psql import * 

#TODO: TEMPORARY - ***** move these to environment variables and put in heroku *****
from my_secrets import API_SECRET_KEY

# ****NEED TO ALSO INSTALL Flask-Reloaded in requirements TO FIX BUGS IN flask_uploads!!!

#TODO:
# from forms import User_registration, User_login, Admin_registration, Admin_login


############################# APP START ##############################

app=Flask(__name__)


# original local postgresql db

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1@localhost:5432/comicswap2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://avxgtkfcevfqzj:a0fbe2cd6e9eec4915e34380038d0774157b76d7d4624ef8549351aa8230b533@ec2-54-159-175-38.compute-1.amazonaws.com:5432/dfv5396fcirk5i'

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


############################# LOGIN/REGISTER ################################

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

    #TODO: TEMPORARY - UPDATE WITH USER FROM LOGIN
    session['current_user']=1
    current_user = session['current_user']

    #query all comics EXCEPT this user
    mycomics = Comic.query.filter(Comic.owner_id == current_user)

    return render_template("mystuff.html", mycomics=mycomics) 



@app.route('/comicdetail/<int:id>', methods=["GET"])
def comicdetail(id):
    """ Comic Detail page - should have links to a specific user's comic with all details and option to edit it
    supply css descriptors to show or hide buttons under comic
    .invisible to not display
    .unclickable to not be able to click
    get here from /mystuff
    """

    session['current_user']=1
    current_user = session['current_user']

    #TODO: make this editable for book owner only

    #query this comic
    comic = Comic.query.get_or_404(id)
         

    # TODO: consider doing this with a template instead?
    """These classes are passed in through Jinja as classes into the html to indicate which buttons to show depending on whether this is a current user's comic
    """
    msg_class= ""
    ofr_trade= ""
    ofr_accept = ""
    have_mailed = ""
    editable = ""

    if comic.owner_id == current_user:
        msg_class = "invisible"
        ofr_trade = "invisible"
        #TODO: make btn visable here if offer is made
        #TODO: make btn visable here for user to show status of mailed/not
    else:
        ofr_accept = "invisible"
        have_mailed = "invisible"
        editable = "invisible"       

    user_flags = {
        "msg_class":msg_class,
        "ofr_trade":ofr_trade,
        "ofr_accept":ofr_accept,
        "have_mailed":have_mailed,
        "editable": editable}  

    return render_template("comic-detail.html", comic=comic, user_flags=user_flags )

#

@app.route('/editcomic/<int:id>', methods=["GET","POST"])
def editcomic(id):
    """ Comic Detail page - should have links to a specific user's comic with all details and option to edit it"""



    session['current_user']=1
    current_user = session['current_user']

    """TODO: make this editable for book owner only with 
        - an edit button that uses JS to toggle the unclickable button on fields
        - code that toggles "You have offers(s) - check them now" button if you have one
    """

    #query this comic
    comic = Comic.query.get_or_404(id) 
    form = EditComicsForm(obj=comic) 

    #check authorization      
    if comic.owner_id == current_user: 

        #form validation  
        if form.validate_on_submit(): 
            comic.title = form.title.data
            comic.issuenumber = form.issuenumber.data
            comic.year = form.year.data 
            comic.price = form.price.data
            comic.publisher = form.publisher.data
            comic.pedigree = form.pedigree.data
            comic.location = form.location.data
            comic. grade = form.grade.data
            comic.email = form.email.data
            comic.notes = form.notes.data  
            comic.assessed_source = form.assessed_source.data         

            db.session.commit()   
            
            flash(f"Comic details updated for { comic.title } # {comic.issuenumber } ")
            return redirect(f"/comicdetail/{comic.id}")         

        else:                   
            return render_template("edit-comic.html", comic=comic, form=form)



    #if authorization fails...
    flash(f"NOT CURRENT USER")
    return render_template("search.html")

    




@app.route('/search', methods=["GET"])
def search():
    """ Search page - should default to most popular titles available, and be able to search books by title, date range, pedigree, condition, price range..."""

    #TODO: TEMPORARY - UPDATE WITH USER FROM LOGIN
    session['current_user']=1
    current_user = session['current_user']

    #query all comics EXCEPT this user
    comics = Comic.query.filter(Comic.owner_id != current_user)

 
    return render_template("search.html", comics=comics)



###############################  MAIL ROUTES #################################

@app.route('/messages', methods=["GET"])
def inbox():
    """ inbox page - should show all messages recieved from members with a mail search box and pagination"""

    #TODO: TEMPORARY - UPDATE WITH USER FROM LOGIN
    session['current_user']=1
    current_user = session['current_user']

    #query all of this user's messages
    messages = Msg.query.filter(Msg.to_id == current_user)
    # senders = User.query.join(Msg).filter(Msg.to_id == current_user)
    # print(senders)
    senders = User.query.all()

    #send to the template as variable
    return render_template("messages.html", messages=messages, senders=senders)


@app.route('/msgsent', methods=["POST"])
def msgsent():
    """ 
    gathers POST data (to_id, mailto, subject, message )
    creates object and writes it to db
    TODO: error handling
    alerts the TO person that a  messages was sent from user 
    create message and send alert to receiver
    """

    current_user=session['current_user']

    #gather POST data
    to_id = request.form["to_id"]
    mailto = request.form["mailto"]
    subject = request.form["subject"]
    message = request.form["message"]
    read=False
    attachments=""
    # msg = Message()
    # message = msg.create(3, " Bob Ross", "this is a test msg", "this is a message just a message of some size to try things out", "attachment details", False)

    new_msg = Msg(to_id=to_id, from_id=current_user, subject=subject, content=message, read=read, attachments=attachments)


    db.session.add(new_msg)
    db.session.commit()

    flash(f'Message mailed successfully to {mailto}')

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


@app.route('/newmail')
def newmail():
    """ write an email page - should show form to create an e-mail and send"""
 
    return render_template("newmail.html")

# @app.route('/reply/<int:fromid>/<msg_num>')
# def reply(fromid, msg_num):
#     """ display an email page with reply to person's e-mail already in place - should show form to create an e-mail and send"""

#     replyto = User.query.get_or_404(fromid)
#     this_msg = Msg.query.get_or_404(msg_num)
 
#     return render_template("reply.html", replyto=replyto, this_msg=this_msg)

@app.route('/reply/<msg_num>')  
def reply(msg_num):
    """ display an email page with reply to person's e-mail already in place - should show form to create an e-mail and send"""

    this_msg = Msg.query.get_or_404(msg_num)
    fromnum = this_msg.from_id
    replyto = User.query.get_or_404(fromnum)  
 
    return render_template("reply.html", this_msg=this_msg, replyto=replyto )

@app.route('/mailowner/<int:comic_id>')     
def mailowner(comic_id):
    """ display an email page with reply to person's e-mail already in place - should show form to create an e-mail and send"""

    this_comic = Comic.query.get_or_404(comic_id)
    this_owner = this_comic.owner_id
    replyto = User.query.get_or_404(this_owner)
 
    return render_template("reply.html", this_msg=this_comic, replyto=replyto )

@app.route('/deletemsg', methods=["GET"])
def deletemsg():
    """ write an email page - should show form to create an e-mail and send"""
 
    return render_template("deletemsg.html")


######################### MAILING LIST ####################################

@app.route('/subscribe', methods=["GET"])
def subscribe():
    """ write an email page - should show form to create an e-mail and send"""
 
# Set up email WTForm validation (route, Model, SubscriptionForm, subscribe.html)

#Client clicks 'subscribe' on button only index.html  
# goes to subscribe.html -> form takes username, e-mail, password (twice) POSTs to /addUser route
# /addUser route 
    # does form validation
        # if valid
            # create password
            # add user/password to db through sqlalchemy
            # e-mail welcome note - API to Mailchimp?
            # 
        # else throw error?  
    # flashes "welcome" and goes to search/main books page



    return render_template("subscribe.html")

########################### TRADING #########################################

@app.route('/offertrade', methods=["GET"])
def offertrade():
    """ 
    - offers user a form to initiate a trade
    -  should have drop-downs indicating options
    - Should have link to their collection with ability to choose more than one
    - 
    - ask client for legalize he wants here
    """
 
    return render_template("offertrade.html")


@app.route('/tradeoffered', methods=["GET"])
def tradeoffered():
    """ show trade offered page - later change for a flash and redirect to prior page(?)
    """
 
    return render_template("tradeoffered.html")




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


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)
    # serve(app)