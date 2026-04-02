import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydbproject.settings')
django.setup()


from myapp.models import Policy

# insert data
Policy.objects.create(
    policy_type="Health",
    name="Hema",
    email="hema@gmail.com",
    phone="9876543210",
    amount=5000
)

# fetch data
data = Policy.objects.all()
for d in data:
    print(d.name, d.policy_type)