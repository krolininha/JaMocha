from flask import Flask, render_template
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

# Server heroku?