from flask import Flask, render_template
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

@app.route('/customer/<gender>')
def customer(gender):
    all_customer = Customer.objects(gender = gender)
    
    ten_customer = find_contacted()[0:10]

    return render_template('customer.html', ten_customer = ten_customer)

if __name__ == '__main__':
  app.run( debug=True)
 