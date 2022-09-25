"""Seed file to make sample data for comicswap2 db."""

from models import db, Msg, User
from app import app

# Create all tables
db.drop_all()
db.create_all()

############################### USERS ####################################
# If table isn't empty, empty it
User.query.delete()

# Add users
usr1 = User(
    username="magiclar", 
    fname="Larry", 
    lname="Volz", 
    email="imaginologist@gmail.com", 
    confirmation_token="OU812",
    confirmed=False,
    blocked=False,
    role=0,
    mailinglist=True
    )

usr2 = User(
    username="comicrodney", 
    fname="Rodney", 
    lname="Chakan", 
    email="something@thecomicswap.com", 
    confirmation_token="ASDF1234",
    confirmed=False,
    blocked=False,
    role=1,
    mailinglist=True
    )

# Add new users to session, so they'll persist
db.session.add(usr1)
db.session.add(usr2)

############################### MESSAGES ####################################
# If table isn't empty, empty it
Msg.query.delete()

# Add messages
msg1 = Msg(to_id=1, from_id=2, subject="first db test of msgs", content="this would be a great place for some lorem ipsum.  But I'll just type up some random content instead.  Okay, that should be enough.", read=False, attachments="{'http://www.test.com', 'http://www.test2.com'}")

msg2 = Msg(to_id=0, from_id=2, subject="2nd db test of msgs", content="MORE TEXT!!!  this would be a great place for some lorem ipsum.  But I'll just type up some random content instead.  Okay, that should be enough.", read=False, attachments="{'http://www.test.com', 'http://www.test2.com'}")

# Add new messages to session, so they'll persist
db.session.add(msg1)
db.session.add(msg2)




# Commit--otherwise, this never gets saved!
db.session.commit()
