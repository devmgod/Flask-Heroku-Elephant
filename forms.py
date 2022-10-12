from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, DateTimeField, IntegerField, StringField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, NumberRange, AnyOf, URL

class EditComicsForm(FlaskForm):
    """
    TODO:  FIX NameError: name 'IntegerField' is not defined

    with all the field definitions.

    """

    owner = StringField("label text", 
        validators = [InputRequired(message = "cannot be blank")])

    comictitle = StringField("label text", 
        validators = [InputRequired(message = "cannot be blank")])


    issuenumber = IntegerField("must be an integer")

    year = IntegerField("must be an integer")

    price = FloatField("must be a number")

    publisher = StringField("label text", 
        validators = [InputRequired(message = "cannot be blank")])

    pedigree = IntegerField("must be an integer")

    location = IntegerField("must be an integer")

    grade = FloatField("must be a number")


    email = StringField("Email", 
        validators = [Optional(), Email()])

    notes = StringField("label text", 
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