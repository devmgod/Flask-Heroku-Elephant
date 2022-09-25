"""Seed file to make sample data for pets db."""

from models import Msg, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Msg.query.delete()

# Add messages
msg1 = Msg(to_id=1, from_id=2, subject="first db test of msgs", content="this would be a great place for some lorem ipsum.  But I'll just type up some random content instead.  Okay, that should be enough.", read=False, attachments="{'http://www.test.com', 'http://www.test2.com'}")

msg2 = Msg(to_id=0, from_id=2, subject="2nd db test of msgs", content="MORE TEXT!!!  this would be a great place for some lorem ipsum.  But I'll just type up some random content instead.  Okay, that should be enough.", read=False, attachments="{'http://www.test.com', 'http://www.test2.com'}")

# Add new objects to session, so they'll persist
db.session.add(msg1)
db.session.add(msg2)

# Commit--otherwise, this never gets saved!
db.session.commit()
