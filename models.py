from uuid import UUID
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

def connect_db(app):
    db.app = app 
    db.init_app(app)

#MODELS GO BELOW
class Msg(db.Model):

    __tablename__ =  "messages"

    id = db.Column(db.Integer,
    primary_key = True,
    autoincrement = True)

    to_id = db.Column(db.Integer,
    nullable = False)

    from_id = db.Column(db.Integer,
    nullable = False)

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
