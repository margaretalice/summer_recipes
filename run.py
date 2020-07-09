import os
from flask import Flask, flash, render_template, redirect,request, session,url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.confi["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ,get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/autumn_recipes')
def autumn_recipes():
    return render_template("autumn_recipes.html")


@app.route('/spring_recipes')
def spring_recipes():
    return render_template("spring_recipes.html")


@app.route('/winter_recipes')
def winter_recipes():
    return render_template("winter_recipes.html")


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    tasks = mongo.db.tasks,find()
    return render_template("tasks.html", tasks = tasks)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
