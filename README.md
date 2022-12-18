# Django

Setup

To set up a Django project, you will need to have Python and Django installed on your computer. If you don't have Python installed, you can download it from the Python website (https://www.python.org/). If you don't have Django installed, you can install it using pip, the Python package manager. Open a terminal window and enter the following command:
pip install Django

Now that you are in the project directory, you can start the Django development server by running the following command:
python manage.py runserver
This will start the development server at http://127.0.0.1:8000/. You can access the Django admin site at http://127.0.0.1:8000/admin/.


Access
There are 5 pages : <br>
Index (http://127.0.0.1:8000/shop/). You can see all the products from here. there is a redirect for each link below.<br>
Create (http://127.0.0.1:8000/shop/create). You can create a new article with this page.<br>
Update (http://127.0.0.1:8000/shop/update/<id>). You can update an existing article from here.<br>
Delete (http://127.0.0.1:8000/shop/delete/<id>). You can delete an existing article in this page.<br>
Show (http://127.0.0.1:8000/shop/<id>). You can see a particular article here.
