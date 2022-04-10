import sqlite3
from flask import request


def get_all_posts():
    connection = sqlite3.connect('blog.sqlite')
    cursor = connection.cursor()

    cursor.execute("SELECT title, description, date FROM posts")
    posts = cursor.fetchall()
    connection.close()
    return posts

def create_post():
    connection = sqlite3.connect('blog.sqlite')
    cursor = connection.cursor()

    title = request.args.get("title")
    description = request.args.get("description")


    cursor.execute(f"INSERT INTO posts (title,description) VALUES (?, ?)", (title,description))
    new_post = connection.commit()
    connection.close()
    return new_post


def update_post():
    connection = sqlite3.connect('blog.sqlite')
    cursor = connection.cursor()

    id = request.args.get("id")
    description = request.args.get("description")

    if id:
        cursor.execute(f"UPDATE posts SET description = ? WHERE id = ?", (description,id))
        updated_post = connection.commit()
        connection.close()
        return updated_post



def delete_post():
    connection = sqlite3.connect('blog.sqlite')
    cursor = connection.cursor()

    id = request.args.get("id")
    if id:
        cursor.execute(f"DELETE FROM posts WHERE id = ?", (id))
        deleted_post = connection.commit()
        connection.close()
        return deleted_post

