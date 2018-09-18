from flask_wtf import FlaskForm
from wtforms import  StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    post = StringField('Your name',validators=[Required()])
    body = TextAreaField('Pitch')
    category = SelectField('category', choices=[('choose', 'choose'),('business', 'business pitch'),('Tech Pitch', 'Tech Pitch'),
    ('Health Pitch', 'Health Pitch')])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):

    post = StringField('Comment title',validators=[Required()])
    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')


class BusinessForm(FlaskForm):
    post = StringField('Your name',validators=[Required()])
    body = TextAreaField('Pitch')
    submit = SubmitField('Pitch')



class TechForm(FlaskForm):
    post = StringField('Your name',validators=[Required()])
    body = TextAreaField('Pitch')
    submit = SubmitField('Pitch')
    


class HealthForm(FlaskForm):
    post = StringField('Your name',validators=[Required()])
    body = TextAreaField('Pitch')
    submit = SubmitField('Pitch')
    
