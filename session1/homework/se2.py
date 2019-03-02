from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "User Name"
Users ={
    "Minh" : 
            {
                "name" : "Nguyễn Đức Minh",
                "age" : 21,
                "adress" : "Hà Nội",
            },
    "Linh" : 
            {
                "name" :"Nguyễn Tùng Linh",
                "age" : 21,
                "adress" : "Hà Nội"
            },
    "Thao" : {
                "name" : "Phạm Thành Thảo",
                "age" : 23,
                "adress" : "Hà Nội"

            }
    }
@app.route("/user/<username>")
def username(username):
    if username in Users:
        return str(Users[username])
    else:
        return " User not found"

if __name__ == '__main__':
    app.run(debug=True)
