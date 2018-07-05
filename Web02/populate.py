from models.service import Service
import mlab
from random import randint, choice
from faker import Faker
from models.user import User


mlab.connect()

# fake = Faker()
# for i in range(50):
#     print("Saving service", i + 1, ".....")
#     new_service = Service(
#         name = fake.name(),
#         yob = randint(1990,2000) ,
#         gender = randint(0,1) ,
#         height = randint(155,190),
#         phone = fake.phone_number(),
#         address = fake.address(),
#         status = choice([True, False])  
#     )


# for i in range(20):
#     print("Saving customer", i + 1, ".....")
#     new_customer = Customer(
#         name = fake.name(),
#         yob = randint(1990,2000) ,
#         gender = randint(0,1) ,
#         phone = fake.phone_number(),
#         email = fake.email(),
#         job = fake.job(),
#         company = fake.company(),
#         contacted = choice([True, False])
#     )

#     new_customer.save()


mlab.connect()

new_service = Service(
    name = "Lương Mạnh",
    yob = 1995,
    gender = 1,
    height = 175,
    phone = "01662595895",
    address = "Hà Nội",
    status = False,
    description = "Đẹp trai, cool ngầu",
    image = "../static/image/manhdeptrai.jpg" ,
    measurements = ["unknow","unknow","unknow"],
)
new_service.save()

new_user = User(
    fullname = "Lương Mạnh",
    email = "aaA",
    username = "admin",
    password = "admin"
)
new_user.save()