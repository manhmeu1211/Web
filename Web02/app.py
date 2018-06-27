from flask import *
app = Flask(__name__)
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer
from query import *


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
    find_id = Service.objects.get(id=service_id)
    return render_template('detail.html', find_id = find_id)


@app.route('/customer/<gender>')
def customer(gender):
    all_customer = Customer.objects(gender = gender)
    
    ten_customer = find_contacted()[0:10]

    return render_template('customer.html', ten_customer = ten_customer)


@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template ('admin.html', all_service = all_service)


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
        )
        find_id.reload()

        return redirect(url_for('admin'))         
    

if __name__ == '__main__':
      app.run( debug=True)
 