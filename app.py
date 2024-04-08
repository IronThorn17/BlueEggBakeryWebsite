from flask import Flask, request, jsonify, render_template
from livereload import Server
import json
import os

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
    # Read cart data from cart.json
    with open('cart.json', 'r') as cart_file:
        cart_data = json.load(cart_file)

    # Read product data from database.json
    with open('database.json', 'r') as database_file:
        product_data = json.load(database_file)

    # List to store product details with quantities
    cart_items = []

    # Iterate through the items in the cart
    for product_id, quantity in cart_data.items():
        # Find the corresponding product details using the product ID
        product = next((p for p in product_data if p['id'] == int(product_id)), None)
        if product:
            # Add product details along with the quantity to the cart_items list
            cart_items.append({
                'product': product,
                'quantity': quantity
            })

    # Render the cart.html template with cart_items data
    return render_template('cart.html', cart_items=cart_items)

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    # Get the data sent from the client-side JavaScript
    data = request.json

    # Check if cart.json exists and is not empty
    if os.path.exists('cart.json') and os.path.getsize('cart.json') > 0:
        with open('cart.json', 'r') as file:
            cart = json.load(file)
    else:
        cart = {}

    # Check if the product is already in the cart
    if data['product_id'] in cart:
        cart[data['product_id']]['quantity'] += data['quantity']
    else:
        cart[data['product_id']] = {'quantity': data['quantity']}
    
    # Write the updated cart data back to cart.json
    with open('cart.json', 'w') as file:
        json.dump(cart, file)
    
    # Return a success message
    return jsonify({'message': 'Product added to cart successfully'})

@app.route('/remove-from-cart', methods=['POST'])
def remove_from_cart():
    print("remove from cart")
    # Get the product ID to remove from the cart
    product_id = request.json.get('product_id')

    print(product_id)

    # Read cart data from cart.json
    with open('cart.json', 'r') as cart_file:
        cart_data = json.load(cart_file)

    # Remove the Product form the Cart
    if str(product_id) in cart_data:
        del cart_data[str(product_id)]

        with open('cart.json', 'w') as cart_file:
            json.dump(cart_data, cart_file)

        return jsonify({'message': 'Product removed from cart successfully'})
    else:
        return jsonify({'error': 'Product not found in cart'}), 404

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
