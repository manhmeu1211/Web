from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello C4E 18"

# @app.route("/bmi/<int:w>/<int:h>")
# def bmi(w, h):
#     bmi = w/((h/100)*2)
#     if bmi < 16:
#         return "Severely underweight"
#     elif   16 <= bmi < 18.5:
#         return "Underweight"     
#     elif   18.5 <= bmi < 25:
#         return "Normal"     
#     elif 25 <= bmi < 30:
#         return "Overweight"
#     else:
#         return "Obese"    
        
@app.route("/bmird/<int:w>/<int:h>")     
def bmi(w, h):
    
    bmi = w/((h/100)*2)
    status = ""
    if bmi < 16:
        status = "Severely underweight"
    elif   16 <= bmi < 18.5:
        status = "Underweight"     
    elif   18.5 <= bmi < 25:
        status = "Normal"     
    elif 25 <= bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"    

    return render_template("bmi.html", bmi = bmi, status = status )
            
    








if __name__ == '__main__':
  app.run(debug=True)