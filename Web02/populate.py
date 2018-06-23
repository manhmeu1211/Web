from models.service import Service
import mlab
from random import randint, choice
from faker import Faker
from models.customer import Customer

mlab.connect()

fake = Faker()
for i in range(50):
    print("Saving service", i + 1, ".....")
    new_service = Service(
        name = fake.name(),
        yob = randint(1990,2000) ,
        gender = randint(0,1) ,
        height = randint(155,190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice([True, False])  
    )

    new_service.save()

for i in range(20):
    print("Saving customer", i + 1, ".....")
    new_customer = Customer(
        name = fake.name(),
        yob = randint(1990,2000) ,
        gender = randint(0,1) ,
        phone = fake.phone_number(),
        email = fake.email(),
        job = fake.job(),
        company = fake.company(),
        contacted = choice([True, False])
    )

    new_customer.save()
