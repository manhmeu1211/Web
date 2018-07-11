from flask import *
app = Flask(__name__)
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer
from query import *
from models.user import User 
from models.order import Order
from datetime import datetime
from gmail import *

app.secret_key = "f*** secret key"
#0 create connection
mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<gender>')
def searchinfo(gender):
    all_service = Service.objects(gender=gender)
    
    return render_template('search.html', all_service = all_service)


@app.route('/detail/<service_id>')
def detail(service_id):
    if "loggedin" in session:
        find_id = Service.objects.get(id=service_id)
        if service_id is None:
            return "Not found"
        else:
            return render_template('detail.html', find_id = find_id)
    else:
        session['service_id'] = service_id
        return redirect(url_for('login'))

@app.route('/customer/<gender>')
def customer(gender):
    all_customer = Customer.objects(gender = gender)
    
    ten_customer = find_contacted()[0:10]

    return render_template('customer.html', ten_customer = ten_customer)


@app.route('/admin')
def admin():
    if "loggedin" in session:
        all_service = Service.objects()
        return render_template ('admin.html', all_service = all_service)
    else:
        return "Yêu cầu đăng nhập"


@app.route('/delete/<service_id>')
def delete(service_id):
    find_id = Service.objects.get(id=service_id)
    if find_id is None:
        return "Id not found"
    else:
        find_id.delete()
        return redirect(url_for('admin'))

@app.route('/new-service', methods = ["GET", "POST"])
def create():
    if request.method =="GET":
        return render_template("newservice.html")
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']
        gender = form['gender']
        new_service = Service (
            name = name,
            yob = yob,
            address = address,
            gender = gender
        )
        new_service.save()
        return redirect(url_for('admin')) 
        
        
@app.route('/update-service/<service_id>', methods = ["GET", "POST"])
def update(service_id):
    if request.method =="GET":
        find_id = Service.objects.get(id=service_id)
        return render_template("update.html", find_id = find_id )
    elif request.method == "POST":
        form = request.form
        find_id = Service.objects.get(id=service_id)
        find_id.update(
            name = form['name'],
            yob = form['yob'],
            address = form['address'],
            gender = form['gender']
        )
        find_id.reload()

        return redirect(url_for('admin'))
        
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form 
        username = form['username']
        password = form['password']
        
        log_user = User.objects.get(username=username)
        if  log_user['password'] == password and log_user['username'] == username:
                session['loggedin'] = True
                user_id = str(log_user['id'])
                session['user_id'] = user_id
                return redirect(url_for('index'))
        else:
            return "Login failed"

@app.route('/logout')
def logout():
    del session['loggedin']
    return redirect(url_for('index'))

@app.route('/order/<service_id>')
def order(service_id):
    new_order = Order(
        service_id = service_id,
        user_id = session['user_id'],
        time_order = datetime.now().strftime("%I:%M %p"),
        is_accepted = False 
    )
    new_order.save()
    return "Send request"

@app.route('/order/accept/<order_id>')
def order_accept(order_id):
    order_id = Order.objects.get(id=order_id)
    if order_id is None:
        return "Not found"
    else:
        order_id.update(
            set_is_accepted = True
        )
        one_order.reload()
        gmail = GMail('Manh<manhmeu1211@gmail.com>','Something')
        content="Your request was accepted by Admin."
        msg = Message('Hello',to=order_id.user_id.email,html=content)
        gmail.send(msg)
        return redirect(url_for('admin_order'))

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        form = request.form
        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']

        new_user = User(
            fullname = fullname,
            email = email,
            username = username,
            password = password
        ) 
        new_user.save()
        return redirect(url_for('index'))

if __name__ == '__main__':
      app.run( debug=True)