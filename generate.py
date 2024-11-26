import os
import random
import django
from string import ascii_letters, digits
from random import choices


from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from main.models import Neighborhood, House

fake = Faker()

Neighborhood.objects.all().delete()
House.objects.all().delete()


a_b = {
    'A':'A',
    'B':'B'
}

a_b = list(a_b.keys())

for _ in range(3):
    neighborhoods = Neighborhood.objects.create(
        title = fake.word().capitalize(),
        chairman = fake.name_male()+' '+fake.last_name_male(),
        MFY = fake.word().capitalize() +' ' + 'MFY',
        people = round(random.uniform(20, 35)),
        area = round(random.uniform(5, 18,),2),
        number_houses = round(random.uniform(4, 4)),

    )


    neighborhoods.save()
neighborhood = Neighborhood.objects.all()




for _ in range(12):
    houses = House.objects.create(
        house_boss = fake.name_male(),
        house_number = round(random.uniform(1, 4)),
        a_b = fake.random_element(a_b),
        people = round(random.uniform(4, 15)),
        area = round(random.uniform(500, 5000), 2),
        neighborhood = fake.random_element(neighborhood)


    )
    houses.save()

