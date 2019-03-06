from flask import Flask, render_template, request
app = Flask(__name__)

bike = [
    {
        "model" : "Ducati",
        "dailyfee(VND) " : 1000000,
        "image" : "https://images.ctfassets.net/x7j9qwvpvr5s/68QJSfINoWUk64YiGmowkM/207cc7e566f70eadd1d4bb61ae2e0d49/Monster-797-Studio-MY19-08-Gallery-1920x1080.jpg",
        "year" : "e.g. 2013"
    }
]
@app.route("/")
def home():
    return render_template("bike.html", bike_list = bike)

@app.route("/new_bike", methods=["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template("new_bike.html")
    elif request.method == "POST":
        form = request.form
        m = form["model"]
        d = form["dailyfee(VND)"]
        i = form["image"]
        y = form["year"]
        new_bike = {
            "model": m,
            "dailyfee(VND)": d,
            "image": i,
            "year": y
        }
        bike.append(new_bike)
        return m + " added " 

if __name__ == '__main__':
  app.run(debug=True)