import os

os.chdir('backend')
os.system('pip install -r requirements.txt')
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
os.system('python manage.py runserver')
