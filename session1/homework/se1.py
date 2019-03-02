from flask import Flask
app = Flask(__name__)

@app.route("/") 
def home(): 
    return "Body Mass Index"

@app.route("/bmi/<int:weight>/<int:height>") #height cm
def bmi(weight,height):
    bmi_= weight/((height*0.01)**2)
    if bmi_ < 16:
        return "Severely underweight"
    elif 16 <= bmi_ < 18.5:
        return " Underweight"
    elif 18.5 <= bmi_ < 25: 
        return "Normal"
    elif 25 <= bmi_ < 30: 
        n = "Overweight"
    elif bmi_ > 30: 
        return  "Obese"

if __name__ == '__main__':
    app.run(debug=True)
