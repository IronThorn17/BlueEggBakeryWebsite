from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Read donut data from the JSON file
    with open('database.json', 'r') as file:
        database = json.load(file)
    return render_template('index.html', database=database)

if __name__ == '__main__':
    app.run(debug=True)