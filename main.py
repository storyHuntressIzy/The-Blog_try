from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, flash
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
#from forms import CommentForm, CreatePostForm, RegisterForm, LoginForm 


app = Flask(__name__)
ckeditor = CKEditor(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
