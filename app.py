from flask import Flask, render_template

app = Flask(__name__)

# Create first webpage :
# route --> my domain is : http://127.0.0.1:5501/
# Function --> What you wanna to show im webpage
# templates --> Stay all html

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/menu")
def menu():
    menu_items = [
        {
            "name": "Cappuccino",
            "price": 4.00,
            "description": "Classic Italian style cappuccino with perfectly steamed milk and rich espresso base.",
            "features": ["Perfect foam", "Double shot", "Italian style"],
            "image": "https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730310933/pexels-helder-quiala-434379851-15293893_pcgyqj.jpg",
            "is_popular": False
        },
        {
            "name": "Matcha Latte",
            "price": 4.75,
            "description": "Premium Japanese matcha green tea with steamed milk for a healthy alternative.",
            "features": ["Organic matcha", "Antioxidant rich", "Smooth taste"],
            "image": "https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730311221/pexels-minan1398-911810_beincj.jpg",
            "is_popular": False
        },
        {
            "name": "Vanilla Frappuccino",
            "price": 5.25,
            "description": "Blended iced coffee with sweet vanilla syrup, topped with whipped cream.",
            "features": ["Vanilla flavor", "Whipped cream", "Blended ice"],
            "image": "https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730311392/pexels-mlkbnl-11976949_jvy0db.jpg",
            "is_popular": True
        },
        {
            "name": "Caramel Macchiato",
            "price": 4.75,
            "description": "Smooth espresso and steamed milk combined with sweet caramel syrup for a delightful treat.",
            "features": ["Caramel drizzle", "Vanilla syrup", "Espresso mark"],
            "image": "https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730311651/pexels-freestocks-214333_o3oynr.jpg",
            "is_popular": True
        },
        {
            "name": "Black Coffee",
            "price": 1.20,
            "description": "Our preferred, straightforward and unique method of developing cool coffee.",
            "features": ["Pure flavor", "Premium beans", "Perfect temperature"],
            "image": "https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730234044/pexels-shameel-mukkath-3421394-5169109_gc9bnx.jpg",
            "is_popular": True
        },
        {
            "name": "Iced Americano",
            "price": 3.50,
            "description": "Chilled espresso topped with cold water and ice for a refreshing coffee experience.",
            "features": ["Extra cold", "Double shot", "No sugar"],
            "image": "https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730233597/pexels-alohaphotostudio-13689963_xbr5n4.jpg",
            "is_popular": False
        },
        {
            "name": "Espresso",
            "price": 1.20,
            "description": "Enjoy a cup of finely brewed espresso from our unique single origin selection for a refreshing start.",
            "features": ["Rich taste", "Full aroma", "Single shot"],
            "image": "https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730310458/pexels-jwmedia-997656_fxmymz.jpg",
            "is_popular": False
        },
        {
            "name": "Mocaccino",
            "price": 3.70,
            "description": "Savor our creamy deluxe cappuccino, crafted with premium milk and freshly ground coffee beans.",
            "features": ["Chocolate flavor", "Creamy milk", "Rich espresso"],
            "image": "https://res.cloudinary.com/dx2gssfoi/image/upload/c_crop,ar_3:4/v1730310060/pexels-chevanon-312418_1_tr4uyn.jpg",
            "is_popular": False
        }
    ]
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