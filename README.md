# Products and Customers' Order App

## Create a virtual environment

- Create a virtual environment by running the command, `mkdir <project_name>` to create project folder
- cd into the project folder `cd <project_folder>`
- run `virtualenv <env_name>` to create environment
cd into the environment and run `<env_name>\Scripts\activate` to activate the virtual environment

## Install django in the environment
- run the command, `pip install django` to install django
- You can run, `django-admin --version` to check the installation

## Creating Django project
- run the command, `django-admin startproject <project_name>` to create a django project
- a new folder with the name you have choosen will have appeared in the project directory
- cd into the project directory
To start server run the command, `python manage.py runserver`.

## Creating the *productOrder* application
- run the command, `python manage.py startapp <your_app_name`. remember the server has to be running
- add the *productOrders* to the list of installed app in settings.py
To access the admin endpoint, magration has to be applied.
- run the command, `python manage.py migrate` to apply migration.
- go to *~<ip_address:port/admin>~* to access the login page.

To create a user
- run the command, `python manage.py createsuperuser`
Follow the prompt to provide *~username~*, *~email_address~* and *~password~*.
The credentials can then be used to login to the ***productOrders*** admin page.

## Create **requirements.txt** file
While your virtualenv is active, run `pip freeze > requirements.txt`. This will generate a .txt file with the list of packages required to run this project.
- to install the requirement.txt contents run, `pip install -r requirement.txt`

## Configure urls and render views
- Open the productOrders/urls.py and create url path to be rendered by the view
- add the path, `path('', views.index, name="index")` to the 'urlpatterns' list. Don't forget to import views .(the same directory)
- goto ***views.py*** file and create your view. In my case, I simply returned an HttpResponse
- goto into *orders/urls.py* and update it to render our productOrders view
- import *include* 
- then do, `path('', include('productOrders.urls'))`
- save and refresh the homepage.

## Creating Template files
- create a folder *templates* in the *productOrders* directory
- go to setting.py and add directory to the templates in the *TEMPLATES* list
- in the *templates* folder, create your *list.html* file
- in views.py, you can return render to render the *list* template
- follow the steps to add any additional 'html' you intend to include

## Creating models 
- go to the *'models.py'* and define your models. 
- define `class Task (models.Model):`
- run `python manage.py makemigrations` and `python manage.py migrate`
- goto *admin.py* and register you models.
- do `from .models import *` to import your models
- do *admin.site.register(Task)* to register your models
- visit the *admin* site and create one or two tasks

## Rendering Models out in the Template
- **Querying the models**
    - go to *views.py* and import models
    - in the *index function* do `tasks = Task.objects.all()` to get all the list of task from db
    - stor in the context dict and pass it to the *render func* as the 3rd parameter.

- **Render the tasks out in the template** ***list**
    - in the *list.html* create a for loop
    - inside template sting `{% %}` don't forget to end the for loop.
    - go and refresh the homepage to see the created tasks.

- **Creating forms using ModelForm**
    - create *forms.py* file in the *productOrders* dir. They are simply form representation of models.
    - do all the necessary imports
    - to create a modelform, define a class
    - define the model you want to create a form for and fields to allow.
    - now that we have the form, lets import it into our template to render it.
    - go to *views.py* and do `from .forms import *` 
    - then do `form = TaskForm()` to instantiate the *TaskForm* class in the function *index*
    - add it to the context dict.
    - go to *list.html* and add this block;
    ```
    <form>
        {% csrf_token %}
        {{form}}
        <input type="submit" name="Create Task">
    </form>
    ```
    - refresh the home page and the form field will appear.
    - notice that the *complete check* was added too.
    - do {{form.title}} for only the *submit* to appear
    - back to *views.py* add the following block
    ```
        if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() #save the user inputs to our db
        return redirect('/')
    ```
- **Adding Edit/Delete Functionality**
    - create a new temp. *task_update.html*
    - create a form field in it
    - go to *views.html* and define the function *updateTask(request, pk)* this view will receive additional parameter *pk* to make it more dynamic.
    - do `task = Task.objects.get(id=pk)` in the function. this will grab the particular task id from the url.
    - go to *productOrders/urls.py* and add the temp. to path dynamically.
    - do `path('task_update/<str:pk>/', views.updateTask, name="task_update")`
    - note that we want to access the *task_update* page from *list.html* therefore go to list and add the link `<a href="{% url 'task_update' task.id %}">Update</a>`
    - do this  `form = TaskForm(instance=task)` in the *updateTask* function in views.py to pass the task into the form field.
    - repeat the following block in the func to grab the POST method and update our table
    ```
        if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    ```

- **Deleting Task**
    - create a new template in the *templates* folder
    - pass the task in this format *{{item}}* 
    - pass a `<a href="{% url 'list' %}">Cancel</a>` and 
    - define the view func for delete temp.
    - pass the delete url path in *urls.py*
    - add the delete link to the *list* template

- **Crossof Completed Task**
    - use condition statement in template tag in the *list.html* template with the following block
    ```
    {% if task.complete == True %}
        <strike> {{task}} </strike>     <!--using strike tag-->
        {% else %}      <!--don't strike through-->
        <span>{{task}}</span>
    {% endif %}
    ```

## Styling with CSS and Bootstrap
The static folder is where we store our css, js and media files including the images and videos
- create a folder *static* in the *songcrud* django project directory
- in it create 3 other folders named *css*, *image*, and *js*
- in the css folder a *main.css* file
- write your main css file here. 
- to link it to your template, first tell django that it exist by going to the *settings.py* file
- scroll down to where you have **STATIC_URL = ...** and add this line of code `STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)`
- add `MEDIA_URL = 'image/'` to reference media files
- remember to import '*os*' at the top
    - ### Linking Static Files
    - add `{% load static %}` at the top of every template file you want to import a static file
    - then a static file is linked using the *link* in this format, `<link rel="stylesheet" href="{% static 'css/main.css' %}">`
    - to link media file use the *img* tag in this format `<img src="{% static "image/logo.jpg" %}" class="logo">`
    - use the *a* link tag `<a class="nav-link" href="{% url 'index' %}">Home<span class="sr-only">(current)</span></a>` to link a clickable link to a page.

## Adding PlaceHolder
- since we are not outputting normal html we can't use the html placeholder tag
- in *forms.py* file, add this code:
`title = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add new task...'}))`

## Hiding Sensitive Credentials using Django-dotenv
- run `pip install python-dotenv` 
- do `from dotenv import load_dotenv`in the *settings.py* file 
- below your import; Initialise environment variables by doing:
- `load_dotenv()`
- create *'.env'* file in the same directory as *settings.py*
- Declare your environmental variables here, don't wrap the values with quotation mark.
-   ```
        SECRET_KEY=h^z13$qr_s_wd65@gnj7a=xs7t05$w7q8!x_8zsld#
        DATABASE_NAME=postgresdatabase
        DATABASE_USER=stone
        DATABASE_PASS=supersecretpassword
    ```
- since using sqlite3 this is what I did:
    ```
        SECRET_KEY=h^z13$qr_s_wd65@gnj7a=xs7t05$w7q8!x_8zsld#
        DATABASE_NAME=<part_of_db_name_in_''>
    ```
- and in the *settings* file, I referenced it thus:
-   ```
        DATABASES = {
        ‘default’: {
        ‘ENGINE’: ‘django.db.backends.postgresql_psycopg2’,
        'NAME': BASE_DIR / str(os.getenv('DATABASE_NAME')),

        <!-- ‘USER’: env(‘DATABASE_USER’),
        ‘PASSWORD’: env(‘DATABASE_PASS’), -->
        }
        }
        SECRET_KEY = str(os.getenv('SECRET_KEY'))
    ```
- add the *.env* file to *.gitignore* using relative path

Visit [Click](https://www.toptal.com/developers/gitignore/api/python) to see more files to add to *.gitignore*
