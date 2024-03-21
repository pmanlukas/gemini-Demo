from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Apple", "price": 1.00},
    {"name": "Orange", "price": 1.50},
    {"name": "Banana", "price": 0.75},
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
