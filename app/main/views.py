from flask import Flask
from . import main
from flask import render_template,redirect, request, url_for,abort,flash
from flask_login import login_required, current_user
from ..models import User,Blog,Comment,Subscribe
from .forms import UpdateProfile,BlogForm,CommentForm,SubscribeForm
from .. import db,photos
from ..email import mail_message


@main.route("/")
def index():
    
    title = 'welcome to blog master'
    blogs = Blog.query.all()

    return render_template('index.html', title= title, blogs = blogs)

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

        
    return redirect(url_for('main.profile',uname=uname))

@main.route('/blog/new', methods=['GET', 'POST'])  
def newblog():
    form= BlogForm()

    if form.validate_on_submit():
        title = form.title.data 
        content = form.content.data 
        category = form.category.data 

        blog = Blog(title = title,content = content, category = category)


        db.session.add(blog)
        db.session.commit()

        blog.save_blog()
        subs = Subscribe.query.all()
        for sub in subs:
            mail_message("New Blog", "email/welcome_subscribe", sub.email)
            return redirect(url_for('main.index'))

        
        flash('Created successfully!')
        return redirect(url_for('main.newblog', id = blog.id))


    return render_template('newblog.html', title='New Blog',blogform = form, blog = 'New Blog')

@main.route('/blog/new/')
def single_blog():
    blog = Blog.query.all()
    return render_template('moreblog.html', blog = blog)

@main.route('/delete/<int:id>')
@login_required
def delete(id):
    del_blog = Blog.query.get(id)
    db.session.delete(del_blog)
    db.session.commit()
    return redirect(url_for('main.index'))    



@main.route('/blog/<int:blog_id>/',methods = ["GET","POST"])
@login_required
def blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id)
    form = CommentForm()

    if form.validate_on_submit():
        title = form.title.data 
        comment = form.comment.data 
        newblog_comment = Comment(title = title,comment=comment,blog_id = blog_id)

        db.session.add(newblog_comment) 
        db.session.commit()

    comments = Comment.query.filter_by(blog_id=blog_id)
    return render_template('comment.html', title = 'You||best blog', blog =blog, blogform = form, comments = comments) 

@main.route('/remove/<int:id>')
@login_required
def remove(id):
    del_comment = Comment.query.get(id)
    db.session.delete(del_comment)
    db.session.commit()
    return redirect(url_for('main.newblog.html'))

@main.route('/subscribe/', methods=['GET','POST'])
def subscribe():
    subForm=SubscribeForm()
    if subForm.validate_on_submit():
        subscribe= Subscribe(email=subForm.email.data,title = subForm.title.data)
        db.session.add(subscribe)
        db.session.commit() 
        return redirect(url_for('main.index')) 
    return render_template('subscription.html',subForm=subForm)    
    














