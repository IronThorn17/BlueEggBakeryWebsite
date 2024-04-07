from flask import Flask, render_template
from livereload import Server
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Read product data from the JSON file
    with open('database.json', 'r') as file:
        products = json.load(file)

    category_products = {}

    for product in products:
        category = product['category']
        if category not in category_products:
            category_products[category] = product

    return render_template('index.html', category_products=category_products)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/category/<string:category>')
def category(category):
    # Read product data from the JSON file
    with open('database.json', 'r') as file:
        products = json.load(file)
    # Filter products based on category
    category_products = [product for product in products if product['category'] == category]
    return render_template('category.html', category=category, products=category_products)

@app.route('/product/<int:product_id>')
def product_details(product_id):
    # Read product data from the JSON file
    with open('database.json', 'r') as file:
        products = json.load(file)
    # Fetch product details based on product_id
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product_details.html', product=product)
    else:
        return "Product not found", 404

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()
    # app.run(debug=True)
