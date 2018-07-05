from flask import *
app = Flask(__name__)
import mlab
from youtube_dl import YoutubeDL
from models.video import Video
app.secret_key = "a fuck*** super secret key"
mlab.connect()



@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos = videos)


@app.route('/detail/<youtube_id>')
def detail(youtube_id):
    
    return render_template('detail.html', youtube_id = youtube_id)


@app.route('/admin', methods = ["GET", "POST"])
def admin():
    if "loggedin" in session:
        if request.method =="GET":
            videos = Video.objects()
            print(videos)
            return render_template('admin.html', videos = videos)
        elif request.method =="POST":
            form = request.form
            link = form['link']
            ydl_opts = {
                'nocheckcertificate' : True,
            }
            ydl = YoutubeDL()
            data = ydl.extract_info(link, download = False)
            print(data)
            title = data['title']
            thumbnail = data['thumbnail']
            views = data['view_count']
            youtube_id = data['id']
            uploader = data['uploader']
            new_video = Video(  title = title, 
                                thumbnail = thumbnail, 
                                views = views, 
                                link = link, 
                                youtube_id = youtube_id, 
                                uploader = uploader)
            new_video.save()
            return redirect(url_for('admin'))
    else:
        return "Yêu cầu đăng nhập"


@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method =="GET":
        return render_template('login.html')
    elif request.method =="POST":
        form = request.form
        username = form['username']
        password = form['password']
        #query
        if username == "admin" and password == "admin":
            session['loggedin'] = True
            return redirect(url_for('index'))
        else:
            return "Login failed"

@app.route('/logout',  methods = ["GET", "POST"])        
def logout():
    del session['loggedin']
    return redirect(url_for('index'))
      
    
if __name__ == '__main__':
      app.run( debug=True)