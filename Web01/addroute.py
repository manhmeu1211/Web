from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello C4E 18"
    
@app.route('/about-me')
def myself():
    info = [
        {
    "name" :"Lương Đức Mạnh",
    "work" : " Fullstack Dev",
    "hobbies" : "Coding, Manga, Anime, Movie, Football, Game, Science",
    "relationship" : "Single",
    "quote"         : "Lạy chúa trên cao. Turn down for what ????",



        },
    ]
    return render_template("myself.html", info = info )



if __name__ == '__main__':
  app.run(debug=True)