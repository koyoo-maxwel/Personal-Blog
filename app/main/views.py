from flask import Flask
from . import main
from flask import render_template,redirect,url_for,abort,request
from flask_login import login_required
#from .. import db,photos
#from .forms import PitchForm,CommentForm,BusinessForm,HealthForm,TechForm
from .forms import BlogForm
from ..models import  User,Blog
from .forms import UpdateProfile
from .. import db




app = Flask(__name__)


# views
@main.route("/")
def index():
    '''
    title = "pitch || pitch it here"
    '''
    title = 'pitch || pich it here'
   

    return render_template('index.html', title= title)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

        return redirect(url_for('main.index'))

        
    return redirect(url_for('main.profile',uname=uname))  


@main.route('/Blog',methods = ['GET','POST'])
@login_required
def Blog():
    form =BlogForm()
    if form.validate_on_submit():     
        db.session.add()
        db.session.commit()
        return redirect(url_for('main.index'))

    # blogs=Blog.query.all()
    return render_template('Blog.html' , form = form )




