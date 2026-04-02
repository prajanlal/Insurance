# import os
# import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
# django.setup()

# from myapp.models import Policy, Claim

# print("Policies:")
# for p in Policy.objects.all():
#     print(p.id, p.name, p.policy_type)

# new_policy = Policy.objects.create(
#     policy_type="Life",
#     name="Ravi",
#     email="ravi@gmail.com",
#     phone="9876543211",
#     amount=10000
# )

# print("Inserted Policy:", new_policy.id)

# claim = Claim.objects.create(
#     policy=new_policy,
#     document="doc1.pdf"
# )

# print("Inserted Claim:", claim.id)


import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

django.setup()

from django.conf import settings
print(settings.DATABASES)   # 👈 ADD THIS LINE

from myapp.models import Policy

for p in Policy.objects.all():
    print(p.name)



import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Policy

# 🔹 INSERT (same as your SQL)
policy = Policy.objects.create(
    policy_type="Health",
    name="Hema",
    email="hema@gmail.com",
    phone="9876543210",
    amount=5000
)

print("Inserted ID:", policy.id)

# 🔹 READ (same as SELECT * FROM policy)
print("\nAll Policies:")
for p in Policy.objects.all():
    print(p.id, p.policy_type, p.name, p.email, p.phone, p.amount)