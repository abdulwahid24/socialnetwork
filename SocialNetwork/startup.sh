python manage.py makemigrations --settings SocialNetwork.settings.local_container \
&& python manage.py migrate --settings SocialNetwork.settings.local_container \
&& echo "from authentication.models import User; User.objects.filter(email='admin@email.com').exists() or User.objects.create_superuser('admin@email.com', 'password');" | python manage.py shell --settings SocialNetwork.settings.local_container\
&& python manage.py runserver 0.0.0.0:8000 --settings SocialNetwork.settings.local_container