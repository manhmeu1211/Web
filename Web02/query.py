from models.service import Service
from models.customer import Customer
import mlab

mlab.connect()

all_service = Service.objects()

# first_service = all_service[0]

# # find_id = Service.objects.get(id='all_service.id')


# # find_id.delete()



all_customer = Customer.objects()

find_contacted = Customer.objects(contacted = False, gender = 1)


