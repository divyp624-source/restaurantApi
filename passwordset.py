import os
import django
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resturant_api_project.settings')
django.setup()
 
from django.contrib.auth.models import User
 
user = User.objects.get(username='admin')
user.set_password('123')
user.save()
 
print("✅ Password updated successfully!")
