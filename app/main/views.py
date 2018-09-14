from flask import Flask
from . import main
from flask import render_template,redirect,url_for,abort,request
from flask_login import login_required
from ..models import User,Pitch,Category
#from .forms import ReviewForm,UpdateProfile
from .. import db,photos
from ..models import  User
from .forms import UpdateProfile




app = Flask(__name__)


# views
@main.route("/")
@login_required
def index():
    '''
    title = "pitch || pitch it here"
    '''
    title = 'pitch || pich it here'
    pitches = Pitch.query.all()

    return render_template('index.html', title= title, pitches = pitches)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

        
    return redirect(url_for('main.profile',uname=uname))  

@main.route('/Blog')
@login_required
def Blog():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'pitch || pitcg it here'
    return render_template('pitch.html', title =title)


@main.route('/Entertainment')
@login_required
def Entertainment():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Entertainment || Blog'
    return render_template('Entertainment.html', title =title)


@main.route('/News')
@login_required
def News():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'pitch ||Category'
    return render_template('category.html', title = title )

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


    
     