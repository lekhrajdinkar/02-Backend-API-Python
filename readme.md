1. download python 3.9 and run setup to install python on machine.
2. create project folder and create virtual env to run your python progarm.
3. python -m venv <dir-name>
4. activate virtaul env
5. use pip install <lib-name> one by one
6. better way to create requirments.txt and list down 3rd party lin
7. add runtime.txt with python version
---
##Django
1. `pip` install django --> it dowload from pypi.org
2. pip install -r `requirments.txt `(add django, rest,etc)
3. `django-admin.py startproject` <project-name> .
4. it will also add `manange`.py for rest of the project schmatics things
5. add apps/subproject : `python manage.py startapp <app-1>`
6. it will add new app/folder with add-1.
7. add entry in `setting.py` for newly added 
---
###Add admin user
1. python manage.py `migrate`
2. python manage.py `createsuperuser`

---
###migration
1. create model ingeri from models.model
2. python manage.py `makemigrations`  app-1
3. python manage.py migrate [app-1]

---
###useful links
- https://pypi.org/project/djangorestframework/
---
##API
###A. APIView
- get,put,post,patch,delete method
- 
###B. View Set
- good to perform CRUD wih database backend
- list,retrive,update,destroy,etc
---

