from flask import Flask
app = Flask(__name__)

# Bind rout to view func
@app.route("/") # route
def home(): #view func
    return "C4E, hello"

@app.route("/myclass")
def myclass():
    return "C4E, this is our class"

@app.route("/hi/<name>")
def hi_minh(name):
    return "Hi " + name

@app.route("/add/<int:so1>/<int:so2>")
def add(so1, so2):
    tong = so1 + so2
    return "Tong la " + str(tong)

items = ["cơm", "phở xào", "bún", "cháo"]
@app.route("/menu")
def menu():
    return str(items)

@app.route("/food/<int:i>")
def food(i):
    return items[i]


if __name__ == '__main__':
  app.run(debug=True)
