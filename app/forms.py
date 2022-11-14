from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, DateTimeField, IntegerField, StringField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, NumberRange, AnyOf, URL

class EditComicsForm(FlaskForm):

    owner = StringField("Owner's Name", 
        validators = [InputRequired(message = "cannot be blank")])

    title = StringField("Title of Comic", 
        validators = [InputRequired(message = "cannot be blank")])


    issuenumber = IntegerField("Issue Number")

    year = IntegerField("Year")

    price = FloatField("Price")

    publisher = StringField("Publisher", 
        validators = [InputRequired(message = "cannot be blank")])

    pedigree = IntegerField("Pedigree")

    location = IntegerField("Location")

    grade = FloatField("Grade")

    assessed_source = StringField("Grading Source", 
        validators = [InputRequired(message = "cannot be blank")])


    email = StringField("Email", 
        validators = [Optional(), Email()])

    notes = StringField("Notes", 
        validators = [InputRequired(message = "cannot be blank")])






    # yes_no = BooleanField("y/n") 
    #form.yes_no.data = True or False

    #states is a list → tuplize it: Id & descrip  same 
    # state = SelectField("state", 
        # choices = [(st, st) for st in states])     

    # category = RadioField("Category", 
    #     [('ic','Ice Cream'), 
    #     ('ch',"potato chips")]) # ul default format

    # dept_code = SelectField("Department Code")
    # choice-tuples added later from postgresql


class SubscriptionForm(FlaskForm):
    
    username = StringField("User Name", 
        validators = [InputRequired(message = "cannot be blank")])
    
    email = StringField("Email", 
        validators = [Optional(), Email()])

    password = StringField("Password", 
        validators = [InputRequired(message = "cannot be blank")])

    