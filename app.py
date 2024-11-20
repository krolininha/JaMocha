from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
import random
import json
import os

app = Flask(__name__)

# Create first webpage :
# route --> my domain is : http://127.0.0.1:5501/
# Function --> What you wanna to show im webpage
# templates --> Stay all html
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'jamocha.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    features = db.Column(db.String(255))
    image = db.Column(db.String(255))
    is_popular = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_features_list(self):
        return [feature.strip() for feature in self.features.split(',')]

def init_db():
    with app.app_context():
        # Cria as tabelas
        db.create_all()

        if Products.query.count() == 0:
            products = [
                Products(
                    name='Cappuccino',
                    price=4.00,
                    description='Classic Italian style cappuccino with perfectly steamed milk and rich espresso base.',
                    features='Perfect foam,Double shot,Italian style',
                    image='https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730310933/pexels-helder-quiala-434379851-15293893_pcgyqj.jpg',
                    is_popular=False
                ),
                Products(
                    name='Matcha Latte',
                    price=4.75,
                    description='Premium Japanese matcha green tea with steamed milk for a healthy alternative.',
                    features='Organic matcha,Antioxidant rich,Smooth taste',
                    image='https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730311221/pexels-minan1398-911810_beincj.jpg',
                    is_popular=False
                ),
                Products(
                    name='Vanilla Frappuccino',
                    price=5.25,
                    description='Blended iced coffee with sweet vanilla syrup, topped with whipped cream.',
                    features='Vanilla flavor,Whipped cream,Blended ice',
                    image='https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730311392/pexels-mlkbnl-11976949_jvy0db.jpg',
                    is_popular=True
                ),
                Products(
                    name='Caramel Macchiato',
                    price=4.75,
                    description='Smooth espresso and steamed milk combined with sweet caramel syrup for a delightful treat.',
                    features='Caramel drizzle,Vanilla syrup,Espresso mark',
                    image='https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730311651/pexels-freestocks-214333_o3oynr.jpg',
                    is_popular=True
                ),
                Products(
                    name='Black Coffee',
                    price=2.70,
                    description='Our preferred, straightforward and unique method of developing cool coffee.',
                    features='Pure flavor,Premium beans,Perfect temperature',
                    image='https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730234044/pexels-shameel-mukkath-3421394-5169109_gc9bnx.jpg',
                    is_popular=True
                ),
                Products(
                    name='Iced Americano',
                    price=3.50,
                    description='Chilled espresso topped with cold water and ice for a refreshing coffee experience.',
                    features='Extra cold,Double shot,No sugar',
                    image='https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730233597/pexels-alohaphotostudio-13689963_xbr5n4.jpg',
                    is_popular=False
                ),
                Products(
                    name='Espresso',
                    price=2.20,
                    description='Enjoy a cup of finely brewed espresso from our unique single origin selection for a refreshing start.',
                    features='Rich taste,Full aroma,Single shot',
                    image='https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730310458/pexels-jwmedia-997656_fxmymz.jpg',
                    is_popular=False
                ),
                Products(
                    name='Mocaccino',
                    price=3.70,
                    description='Savor our creamy deluxe cappuccino, crafted with premium milk and freshly ground coffee beans.',
                    features='Chocolate flavor,Creamy milk,Rich espresso',
                    image='https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730310060/pexels-chevanon-312418_1_tr4uyn.jpg',
                    is_popular=False
                ),
                Products(
                    name='Chocolate Muffin',
                    price=3.50,
                    description='Indulgent double chocolate muffin made with premium cocoa and chocolate chips, freshly baked every morning.',
                    features='Fresh baked,Double chocolate,Moist texture',
                    image='https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1731336989/pexels-anete-lusina-4792413_mjf1st.jpg',
                    is_popular=True
                ),
                Products(
                    name='Butter Croissant',
                    price=3.25,
                    description='Traditional French butter croissant with a flaky, golden-brown crust and soft, layered interior.',
                    features='Handmade daily,Pure butter,Flaky layers',
                    image='https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1731337120/pexels-elkady-3892469_ug15t6.jpg',
                    is_popular=True
                ),
                Products(
                    name='Cinnamon Roll',
                    price=4.00,
                    description='Soft, swirled pastry filled with cinnamon-sugar and topped with chocolate cream.',
                    features='House-made frosting,Warm served,Rich cinnamon',
                    image='https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1731337590/pexels-pixabay-267308_lxr2qv.jpg',
                    is_popular=False
                ),
                Products(
                    name='Bagel Bacon & Egg',
                    price=6.50,
                    description='Freshly toasted bagel filled with crispy bacon, fried egg, melted cheese, and signature sauce.',
                    features='Premium bacon,Free-range egg,Artisanal bagel',
                    image='https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1731337805/pexels-kelly-1179532-14300536_ai5piv.jpg',
                    is_popular=True
                )
            ]
            
            # Adiciona os produtos ao banco de dados
            db.session.add_all(products)
            db.session.commit()
            print("Banco de dados inicializado com sucesso!")


# Route created

@app.route("/")
def homepage():
    with open('data/testemonials.json', 'r') as file:
        data = json.load(file)
        testimonials = random.sample(data['testimonials'], 3)
    return render_template("index.html", testimonials=testimonials)

@app.route("/menu")
def menu():
    menu_items = Products.query.all()
    print("Produtos encontrados:", len(menu_items))
    return render_template("menu.html", menu_items=menu_items)


@app.route("/ourcoffee")
def ourcoffee():
    return render_template("ourcoffee.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")




# Deploy
if __name__ == "__main__":
    init_db()  # Inicializa o banco de dados
    app.run(debug=True)

# Server heroku must pay, better Render....I will learn how it works!!