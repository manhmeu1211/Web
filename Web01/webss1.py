from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
    "title" :"Thơ con cóc",
    "content" : "Trăng hôm nay cao quá. Anh muốn hôn vào má ",
    "author" : "  Some one",
    "gender" : 0

        },
        {
    "title" :"Nhà sàn",
    "content" : "Hôm nay căn nhà sàn vắng. Anh tặng em kỉ niệm đầu",
    "author" : "  NVH",
    "gender" : 1
        }
    ]
    
    return render_template("index.html", posts = posts )


# @app.route("/hello")
# def sayhello():
#     return "Hello m*ther f*cker"

# @app.route("/sayhi/<name>/<age>")
# def sayhi(name, age):
#     return "Hi {0}, you're {1} years old".format(name, age)

# @app.route("/sum/<int:x>/<int:y>")
# def calc(x, y):
#     return str(x + y)

if __name__ == '__main__':
  app.run(debug=True)
 

