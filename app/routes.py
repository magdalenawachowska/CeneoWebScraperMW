
from app import app
from flask import render_template

@app.route('/')                  #sciezki - wywolana zostanie funkcja ponizej
def index():
    return render_template("index.html.jinja")

#zeby uruchomic flaska w trybie debugowanie mamy:
#flask run --debug

@app.route('/extract')                 
def extract():
    return render_template("extract.html.jinja")

@app.route('/products')                 
def products():
    return render_template("products.html.jinja")

@app.route('/author')                 
def author():
    return render_template("author.html.jinja")

@app.route('/product/<product_id>')
def product_id(product_id):
    return render_template("product_id.html.jinga", product_id= product_id)
