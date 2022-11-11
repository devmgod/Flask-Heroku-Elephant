"""Seed file to make sample data for comicswap2 db."""

from models import db, Msg, User, Comic, Offer, Deal
# import Comics-offers
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
    mailinglist=True,
    password="testPassword1"
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
    mailinglist=True,
    password="testPassword2"
    )

# Add new users to session, so they'll persist
db.session.add(usr1)
db.session.add(usr2)

############################### MESSAGES ####################################
# If table isn't empty, empty it
Msg.query.delete()

# Add messages
msg1 = Msg(to_id=1, from_id=2, subject="first db test of msgs", content="this would be a great place for some lorem ipsum.  But I'll just type up some random content instead.  Okay, that should be enough.", read=False, attachments="{'http://www.test.com', 'http://www.test2.com'}")

msg2 = Msg(to_id=2, from_id=1, subject="NOT FOR USER #1 - 2nd db test of msgs", content="MORE TEXT!!!  this would be a great place for some lorem ipsum.  But I'll just type up some random content instead.  Okay, that should be enough.", read=False, attachments="{'http://www.test.com', 'http://www.test2.com'}")

msg3 = Msg(to_id=1, from_id=2, subject="2nd msg for user 1", content="this would be a great place for some lorem ipsum.  But I'll just type up some random content instead.  Okay, that should be enough.", read=False, attachments="{'http://www.test.com', 'http://www.test2.com'}")

# Add new messages to session, so they'll persist
db.session.add(msg1)
db.session.add(msg2)
db.session.add(msg3)


############################### OFFERS ####################################
# If table isn't empty, empty it
Offer.query.delete()

# Add offers
ofr1 = Offer(title="Fantastic 4 for your Batman",num_comics_offered=1,user_offering=2,user_owner=1,owner_response=0,deal_id=0,payment_offer=0,additional_terms="Contingent on pedigree being confirmed.")

ofr2 = Offer(title="Captain America for your Amazing Spiderman",num_comics_offered=1,user_offering=1,user_owner=2,owner_response=0,deal_id=0,payment_offer=0,additional_terms="Looking forward to the deal.")

ofr3 = Offer(title="Superman for your Doctor Strange",num_comics_offered=1,user_offering=2,user_owner=1,owner_response=0,deal_id=0,payment_offer=0,additional_terms="Assuming it's not cursed by an evil trans-dimensional demon.")


# Add new messages to session, so they'll persist
db.session.add(ofr1)
db.session.add(ofr2)
db.session.add(ofr3)


 ############################# comics-offers ##############################
#  TODO: For future development - so people can trade more than one comic at a time
# Comics_offers.query.delete()

# c_o1 = Comics_offers(offer_id=1, comic_id=)



############################### COMICS ####################################
# If table isn't empty, empty it
Comic.query.delete()

# Add messages
comic1 = Comic(owner_id=1, title="Batman", issuenumber=265, cgc_grade=9.6,assessed_value=40.0, assessed_source="CGC", thumbnail="../static/images/batman-p-500.jpg", cover_pic="../static/images/batman-p-1080.jpg", back_cover_pic="", extra_media="", publisher="DC", year=1975, notes="Title is Batman's greatest failure", signed=True, pedigree=1, location=0)

comic2 = Comic(owner_id=1, title="Captain America", issuenumber=100, cgc_grade=9.9,assessed_value=5400, assessed_source="CGC", thumbnail="../static/images/captain_america-p-250.jpg", cover_pic="../static/images/captain_america-p-1080.jpg", back_cover_pic="", extra_media="", publisher="Marvel", year=1968, notes="Title is 'Big Premier Issue'", signed=False, pedigree=2, location=0)

comic3 = Comic(owner_id=1, title="Doctor Strange", issuenumber=50, cgc_grade=9.9,assessed_value=9.99, assessed_source="CGC", thumbnail="../static/images/Dr_strange-p-250.jpg", cover_pic="../static/images/Dr_strange-p-100.jpg", back_cover_pic="", extra_media="", publisher="Marvel", year=1993, notes="Holographic giant issue Guest starring Ghost Rider, Hulk and Silver Surfer'", signed=False, pedigree=3, location=0)

comic4 = Comic(owner_id=2, title="Fantastic 4", issuenumber=52, cgc_grade=9.9,assessed_value=4000, assessed_source="CGC", thumbnail="../static/images/fantastic4_and_black_panther-p-250.jpg", cover_pic="../static/images/fantastic4_and_black_panther-p-1080.jpg", back_cover_pic="", extra_media="", publisher="Marvel", month="July", year=1966, notes="Featuring Black Panther", signed=False, pedigree=4, location=0)

comic5 = Comic(owner_id=2, title="Amazing Fantasy Featuring Spider-Man", issuenumber=15, cgc_grade=9.0,assessed_value=1100000, assessed_source="CGC", thumbnail="../static/images/spider_man_coolest_pic-p-250.jpg", cover_pic="../static/images/spider_man_coolest_pic.jpg", back_cover_pic="", extra_media="", publisher="Marvel", month="August", year=1962, notes="First appearance of Spider-Man", signed=False, pedigree=5, location=0)

comic6 = Comic(owner_id=2, title="Action Comics featuring Superman", issuenumber=419, cgc_grade=9.0,assessed_value=6.0, assessed_source="CGC", thumbnail="../static/images/superman-p-250.jpg", cover_pic="../static/images/superman-p-1080.jpg", back_cover_pic="", extra_media="", publisher="Marvel", month="August", year=1972, notes="First appearance of Spider-Man", signed=False, pedigree=5, location=0)

# Add new messages to session, so they'll persist
db.session.add(comic1)
db.session.add(comic2)
db.session.add(comic3)
db.session.add(comic4)
db.session.add(comic5)
db.session.add(comic6)


# Commit--otherwise, this never gets saved!
db.session.commit()


############################### DEALS ####################################
# If table isn't empty, empty it
Deal.query.delete()

# Add deals
deal1 = Deal(date_of_agreement="2022-11-10 17:00:00.0", amt_owed_seller=0, amt_paid_to_seller=0, amt_owed_comicswap=12.50, amt_paid_comicswap=0, payment_status=0, offer_id=1, delivery_status=0, comic_condition=0)


# Add new messages to session, so they'll persist
db.session.add(deal1)
# db.session.add(deal2)
# db.session.add(deal3)

# Commit--otherwise, this never gets saved!
db.session.commit()
