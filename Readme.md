#Django project JWT

Steps to run the project

1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py createsuperuser
4. python manage.py runserver


Links:
1. Register new user (POST):/user/register/
2. Get Auth Token (POST) params:username/email, password): /api/token/
3. Get all the category details (GET) : /category/
4. Get single category (GET): /category/<category_id>
5. Create new category (POST): /category/add/
6. Update category (PATCH): /category/update/<category_id>
7. Delete category (DELETE): /category/delete/<category_id>