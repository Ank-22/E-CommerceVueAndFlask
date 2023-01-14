from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})
#CORS(app, resources={r'/*':{'origins':'http://localhost:8080',"allow_headers":"Access-Control-Allow-Origin"}})

@app.route('/',methods=['GET'])
def greetings():
    return render_template("index.html")

@app.route('/checkout',methods=['GET'])
def checkout():
    return render_template("checkout.html")

@app.route('/login',methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/contact',methods=['GET'])
def contact():
    return render_template("contact.html")

@app.route('/register',methods=['GET'])
def register():
    return render_template("register.html")

@app.route('/blog',methods=['GET'])
def blog():
    return render_template("blog.html")

@app.route('/article',methods=['GET'])
def article():
    return render_template("article.html")

@app.route('/shop',methods=['GET'])
def shop():
    return render_template("shop.html")

if __name__ == "__main__":
    app.run(debug=True)