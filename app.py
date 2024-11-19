from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import json
import os

app = Flask(__name__)

# Create first webpage :
# route --> my domain is : http://127.0.0.1:5501/
# Function --> What you wanna to show im webpage
# templates --> Stay all html

# Function JSON
def load_menu():
    json_path = os.path.join(app.root_path, 'data', 'menu.json') # safe way to json
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data['menu_items']
#json_path = app.root_path + '/data/menu.json'  (Can fail in Windows)

# models.py

db = SQLAlchemy()

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    features = db.Column(db.JSON)
    image = db.Column(db.String(255))
    is_popular = db.Column(db.Boolean, default=False)



# Route created

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/menu")
def menu():
    menu_items = load_menu()
    return render_template("menu.html", menu_items=menu_items)


@app.route("/ourcoffee")
def ourcoffee():
    return render_template("ourcoffee.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")




# Deploy
if __name__ == "__main__":
    app.run(debug=True)

# Server heroku must pay, better Render....I will learn how it works!!