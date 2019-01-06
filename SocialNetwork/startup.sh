python manage.py makemigrations && python manage.py migrate \
&& echo "from authentication.models import User; User.objects.filter(email='admin@email.com').exists() or User.objects.create_superuser('admin@email.com', 'password');" | python manage.py shell \
&& python manage.py runserver 0.0.0.0:8000 --settings SocialNetwork.settings.local_container