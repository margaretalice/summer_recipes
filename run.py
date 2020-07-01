import os
from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
