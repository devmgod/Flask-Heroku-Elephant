from uuid import UUID
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db=SQLAlchemy()

def connect_db(app):
    db.app = app 
    db.init_app(app)

#MODELS 

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

    confirmation_token = db.Column(db.String(50))

    confirmed = db.Column(db.Boolean, 
    default=False)

    blocked = db.Column(db.Boolean, 
    default=False)

    mailinglist = db.Column(db.Boolean,
    default=False)

    #TODO: relate to roles table
    role = db.Column(db.Integer,
    nullable=False
    )

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    def __repr__(self):
            p = self
            return f"< id={p.id}>"

############################# ROLES ######################################

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



    # from_id = db.Column(db.Integer,
    # db.ForeignKey('users.id'),
    # nullable = False)

    # maildate = db.Column(db.DateTime, nullable=False,
    # default=datetime.utcnow)



    # sender = db.relationship('User')


    # content = db.Column(db.Text,
    # nullable = False)

    # read = db.Column(db.Boolean,
    # default = False)

    # attachments = db.Column(db.Text)

    @classmethod
    # def get_all_unread(cls):
    #     return cls.query.filter(Msg.read == True ).all()

    def __repr__(self):
            p = self
            return f"<Message id={p.id} to_id={p.to_id} from_id={p.from_id} subject={p.subject} content={p.content} read={p.read} attachments={p.attachments}>"


############################# DEALS ####################################

############################# OFFERS ####################################

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

############################# PEDIGREES ###############################

############################# ARTICLES #############################