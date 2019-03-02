from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route("/")
def home():
    return "My Website"

@app.route("/about-me")
def about_me():
    return "Tên tôi là Minh, hiện đang học Toán ứng dụng tại trường đại học Thăng Long, sở thích của tôi là xe, tìm hiểu về xe.....Tôi rất thích chó và mèo, không có người yêu nhưng có chó hoặc mèo là được"
    
@app.route("/school")
def school():
    return redirect("http://techkids.vn/")

if __name__ == '__main__':
    app.run(debug=True)
