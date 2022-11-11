from uuid import UUID
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db=SQLAlchemy()

def connect_db(app):
    db.app = app 
    db.init_app(app)


#MODELS 

############################# ARTICLES (optional/later) #############################

# title - text
#content - rich text
# rating number
# relation to user


############################ TAGS (optional/later) #################################
# tag name
# id

#############################tags-articles (optional/later) ########################
# id
# tagId
# ArticleId


############################# COMICS ######################################

class Comic(db.Model):

    __tablename__ =  "comics"

    id = db.Column(db.Integer,
    primary_key = True,
    autoincrement = True)

    # trades table will show other user involved and ownership changes during a trade
    owner_id = db.Column(db.Integer,
    db.ForeignKey('users.id'),
    nullable = False)

    owner = db.relationship('User')

    title = db.Column(db.String(50),
    nullable=False)

    issue_num = db.Column(db.Integer,
    nullable = False)

    cgc_grade = db.Column(db.Float)

    assessed_value = db.Column(db.Float)

    assessed_source = db.Column(db.String(50), default="CGC")

    thumbnail = db.Column(db.Text)

    cover_pic = db.Column(db.Text)

    back_cover_pic = db.Column(db.Text)

    extra_media = db.Column(db.Text)

    publisher = db.Column(db.Text)

    month = db.Column(db.String(10))

    year = db.Column(db.Integer)

    notes = db.Column(db.Text)

    signed = db.Column(db.Boolean)

    #TODO: MAKE/RELATE TO PEDIGREE TABLE
    pedigree = db.Column(db.Integer) 

    #TODO: MAKE/RELATE TO LOCATION TABLE
    #outgoing, home is 0, at comic-swap, etc.
    location = db.Column(db.Integer, default=0)


    @classmethod
    # def get_all_unread(cls):
    #     return cls.query.filter(Msg.read == True ).all()

    def __repr__(self):
            p = self
            return f"<Message id={p.id} to_id={p.to_id} from_id={p.from_id} subject={p.subject} content={p.content} read={p.read} attachments={p.attachments}>"


############################# DEALS ####################################

class Deal(db.Model):
    __tablename__ =  "deals"

    # id
    id = db.Column(db.Integer,
    primary_key = True,
    autoincrement = True)

    # date_of_agreement
    date_of_agreement = db.Column(db.Date, nullable = False)

    # amt_owed_seller - float - optional assuming a monetary component 
    amt_owed_seller = db.Column(db.Float)

    # amt_paid_to_seller - ""
    amt_paid_to_seller = db.Column(db.Float)

    # amt_owed_comicswap
    amt_owed_comicswap = db.Column(db.Float)

    # amt_paid_comicswap
    amt_paid_comicswap = db.Column(db.Float)

    # date paid
    date_paid = db.Column(db.Date)

    # payment_status - enumeration/number 0=unpaid, 1=paid
    payment_status = db.Column(db.Float)

    # offer relation number unique
    offer_id = db.Column(db.Integer)

    # delivery_status - 0=not mailed, 1=in transit to comicswap, 2=unknown, 3=received by comicswap/uninspected, 4=received/inspected, 5=in-transit to final destination, 6=received at final destination, 7=in-transit returning rejected book, 8=returned to sender
    delivery_status = db.Column(db.Integer)

    # comic_condition = 0=unknown, 1=as promised/accepted, 2=not as promised/discussions, 3=not as promised/rejected, 4=compromised/accepted
    comic_condition = db.Column(db.Integer)


############################# OFFERS ####################################

class Offer(db.Model):
    __tablename__ =  "offers"

    # id
    id = db.Column(db.Integer,
    primary_key = True,
    autoincrement = True)

    # title
    title = db.Column(db.String(50),
    nullable=False)

    # num_comics_offered  - using the comics-offers table users can offer more than one comic in trade for this one
    num_comics_offered = db.Column(db.Integer)

    # user_offering - relation with user making the offer
    user_offering = db.Column(db.Integer)

    # user_receiving - user receiving this offer
    user_owner = db.Column(db.Integer)

    # owner_response - enumeration - most recent response 
    # 0 default = not responded yet, 1=yes/deal made, 2=in negotiations, 3=no, 4=block/report spam
    owner_response = db.Column(db.Integer)

    # deal_id - relation with deal_id (default=0)
    deal_id = db.Column(db.Integer)

    # payment_offer - float amount of money offered (if applicable) in addition to comics offered
    payment_offer = db.Column(db.Float)

    # additional_terms - text, includes additional comics, etc.
    additional_terms = db.Column(db.String(150))


############################# comics-offers #############################

class Comics_offers(db.Model):
    __tablename__ =  "comics_offers"

    # relation id
    id = db.Column(db.Integer,
    primary_key = True,
    autoincrement = True)

    # offer_id
    offer_id = db.Column(db.Integer)

    #comic_id
    comic_id = db.Column(db.Integer)


############################# PEDIGREES ###############################
# actually - can just set up a drop-down where needed and make this an updatable db later as an option


############################# ROLES ######################################

# Currently handled under users

############################# USERS ######################################

class User(db.Model):

    __tablename__ =  "users"

    id = db.Column(db.Integer,
    primary_key = True,
    autoincrement = True)

    username = db.Column(db.String(50),
    nullable=False,
    unique=True)

    fname = db.Column(db.String(50),
    nullable = False)

    lname = db.Column(db.String(50),
    nullable = False)

    email = db.Column(db.String(50),
    unique=True,
    nullable = False)

    password = db.Column(db.String(50),
    unique=True,
    nullable = False)

    confirmation_token = db.Column(db.String(50))

    confirmed = db.Column(db.Boolean, 
    default=False)

    blocked = db.Column(db.Boolean, 
    default=False)

    mailinglist = db.Column(db.Boolean,
    default=False)

    #TODO: optional: relate to a separate roles table
    role = db.Column(db.Integer,
    nullable=False
    )

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    def __repr__(self):
            p = self
            return f"< id={p.id}>"





############################# WATCHLIST #################################
# connects comics and user


############################# MESSAGES #################################
class Msg(db.Model):

    __tablename__ =  "messages"

    id = db.Column(db.Integer,
    primary_key = True,
    autoincrement = True)

    maildate = db.Column(db.DateTime, nullable=False,
    default=datetime.utcnow)

    to_id = db.Column(db.Integer,
    nullable = False)

    from_id = db.Column(db.Integer,
    db.ForeignKey('users.id'),
    nullable = False)

    sender = db.relationship('User')

    subject = db.Column(db.String(50),
    nullable=False)

    content = db.Column(db.Text,
    nullable = False)

    read = db.Column(db.Boolean,
    default = False)

    attachments = db.Column(db.Text)

    @classmethod
    def get_all_unread(cls):
        return cls.query.filter(Msg.read == True ).all()

    def __repr__(self):
            p = self
            return f"<Message id={p.id} to_id={p.to_id} from_id={p.from_id} subject={p.subject} content={p.content} read={p.read} attachments={p.attachments}>"

