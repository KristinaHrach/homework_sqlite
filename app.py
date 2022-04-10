""" sqlite3 blog.sqlite --create database
CREATE TABLE posts (id integer primary key autoincrement, title varchar (400), description varchar(3000), date timestamp default current_timestamp not null);
"""


from flask import Flask, render_template, redirect
from models import get_all_posts, create_post, delete_post, update_post

app = Flask(__name__)

@app.get('/posts')
def posts():
    """Show all posts including their 'title', 'description', and 'date'
    in template 'posts'"""
    posts = get_all_posts()
    return render_template('posts.html', posts = posts)


@app.get('/posts/add')
def new_post():
    """ Add new post using two params 'title' and 'description'. Then redirect
    it to the main page """
    create_post()
    return redirect('/posts')


@app.get('/posts/update')
def changed_post():
    """ Edit description of post using 'id' parameter.Then redirect
    it to the main page"""
    update_post()
    return redirect('/posts')



@app.get('/posts/delete')
def remove_post():
    """ Delete post using 'id' parametr. Then redirect
    it to the main page"""
    delete_post()
    return redirect('/posts')
