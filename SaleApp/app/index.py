from flask import Flask, render_template
from app import app
from app import dao

@app.route('/')
def index():
    categories = dao.load_categories()
    products = dao.load_products()
    return render_template('index.html', categories=categories, products = products)

if __name__ == "__main__":
    app.run(debug=True)