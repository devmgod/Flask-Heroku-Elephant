import json
import requests

class Articles:
    def __init__(self):
        self.api_url = "http://localhost:1337/api"

    def create(self, title, content, rating, user_id, tags):
        #create an article (generate it's own unique id)
        #return the id number and all fields 
        return

    def get_all(self):
        #get all articles and return as json
        r = requests.get(self.api_url + "/articles")
        return r.json() 

    def get_one(self, id):
        #get one article and return all fields as json
        return

    def update(self, id, title, content, rating, user_id, tags):
        #update one article by id - other fields are optional
        #return all fields (updated) as json
        return

    def delete(self, id):
        #delete one article by id 
        #return true if deleted false if not
        return 


class Comics:
    def __init__(self):
        self.api_url = "http://localhost:1337/api"

    def create(self, title, issue_num, cgc_grade, assessed_value, assessed_source, thumbnail, cover_pic, location, users_permissions_user, back_cover_pic, additional_media, Publisher, year, notes, signed, offers):
        #create a comic (generate it's own unique id)
        #some of the above fields are optional (see definitions in strapi)
        #return the id number and all fields as json
        return

    def get_all(self):
        #get all comics and return as json
        return 

    def get_one(self, id):
        #get one comic and return all fields as json
        return

    def update(self, id, title, content, rating, user_id, tags):
        #update one comic by id - other fields are optional
        #return all fields (updated) as json
        return

    def delete(self, id):
        #delete one comic by id 
        #return true if deleted false if not
        return 
    

class Deals:
    def __init__(self):
        self.api_url = "http://localhost:1337/api"

    def create(self, payment_status, offer):
        #create a deal (generate it's own unique id)
        #return the id number and all fields as json
        return

    def get_all(self):
        #get all deals and return as json
        return 

    def get_one(self, id):
        #get one comic and return all fields as json
        return

    def update(self, payment_status, offer):
        #update one deal by id - other fields are optional
        #return all fields (updated) as json
        return

    def delete(self, id):
        #delete one deal by id 
        #return true if deleted false if not
        return 
    

class Message:
    def __init__(self):
        self.api_url = "http://localhost:1337/api"

    def create(self, users_permissions_user, to, subject, content, attachments, read):
        #create a message (generate it's own unique id)
        #some of the above fields are optional (see definitions in strapi)
        #return the id number and all fields as json
        return

    def get_all(self):
        #get all messages for current user and return as json
        return 

    def get_one(self, id):
        #get one message for this user and return all fields as json
        return

    def update(self, users_permissions_user, to, subject, content, attachments, read):
        #update one message for this user by id - other fields are optional
        #return all fields (updated) as json
        return

    def delete(self, id):
        #delete one message by id 
        #return true if deleted false if not
        return 

class Offer:
    def __init__(self):
        self.api_url = "http://localhost:1337/api"

    def create(self, title, requests, trade_offers, user_responding, response, deal, payment_offer):
        #create an offer (generate it's own unique offer_id)
        #some of the above fields are optional (see definitions in strapi)
        #return the id number and all fields as json
        return

    def get_all(self):
        #get all offers for current user and return as json
        return 

    def get_one(self, id):
        #get one offer for this user and return all fields as json
        return

    def update(self, title, requests, trade_offers, user_responding, response, deal, payment_offer):
        #update one offer for this user by id - other fields are optional
        #return all fields (updated) as json
        return

    def delete(self, id):
        #delete one offer by id 
        #return true if deleted false if not
        return 


class Pedigree:
    def __init__(self):
        self.api_url = "http://localhost:1337/api"

    def create(self, title, description, comic, media):
        #create a pedigree (generate it's own unique id)
        #some of the above fields are optional (see definitions in strapi)
        #return the id number and all fields as json
        return

    def get_all(self):
        #get all pedigrees and return as json
        return 

    def get_one(self, id):
        #get one pedigree and return all fields as json
        return

    def update(self, title, requests, trade_offers, user_responding, response, deal, payment_offer):
        #update one pedigree by id - other fields are optional
        #return all fields (updated) as json
        return

    def delete(self, id):
        #delete one pedigree by id 
        #return true if deleted false if not
        return 


class User:
    def __init__(self):
        self.api_url = "http://localhost:1337/api"

    def create(self, username, email, provider, password, resetPasswordToken, confirmation Token, confirmed, blocked, role, articles, comics, messages, responding_user):
        #create a User (generate it's own unique id)
        # (see definitions in strapi)
        #return the id number and all fields as json
        return

    def get_all(self):
        #get all users and return as json
        return 

    def get_one(self, id):
        #get one user and return all fields as json
        return

    def update(self,  username, email, provider, password, resetPasswordToken, confirmation Token, confirmed, blocked, role, articles, comics, messages, responding_user):
        #update one user by id - other fields are optional
        #return all fields (updated) as json
        return

    def delete(self, id):
        #delete one user by id 
        #return true if deleted false if not
        return 

