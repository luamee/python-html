from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Luna'}
    posts = [
        {'author': {'username': 'Lua'}, 'body': "Olá da Lua"},
        {'author': {'username': 'Luo'}, 'body': "Oizinho faces!"}
    ]
    return render_template("index.html", user=user, posts=posts)