from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello C4E 18"
    
@app.route('/user/<username>')
def info(username):
    profile = {

        "manh":{

            "name" :"Lương Đức Mạnh",
            "age" : "23",
            "work" : " Fullstack Dev",
            "school" : "Techkids C4E18 and ĐH Thủy lợi",
            "hobbies" : "Coding, Manga, Anime, Movie, Football, Game, Science",
            "gender" :"",
            "gender1" : 1

            },
        "hoang":{

            "name" :"Nguyễn Văn Hoàng",
            "age" : "21",
            "work" : " Frontend Dev",
            "school" : "Techkids C4E18 and ĐH Thủy lợi",
            "hobbies" : "Coding, Football, watch porn movie",
            "gender" :"",
            "gender1" : 1

            },

        "dong": {

            "name" :"Ngô Thiếu Gia",
            "age" : "21",
            "work" : " Frontend Dev",
            "school" : "Techkids C4E18 and ĐH Thủy lợi",
            "hobbies" : "Coding, querwty, watch porn movie",
            "gender" :"",
            "gender1" : 0
            },
    }
    
    if username in profile:
        
        user = profile[username]

        return render_template("user.html", user = user )

    else:
        return "<b> User not found </b>"


if __name__ == '__main__':
  app.run(debug=True)