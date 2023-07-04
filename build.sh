#Install dependencies
pipenv install

python manage.py collectstatic --no-input

#Run migrations
python3 manage.py migrate