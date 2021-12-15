###### Proyecto de Ciclo IV: Tienda de alquiler de Disfraces
Este proyecto está enfocado en la creación de una página web que permita de forma sistemática el alquiler de disfraces y en una versión siguiente de manera adicional el alquiler de trajes, el valor agregado está en la personalización de los disfraces, adicional a la opción de alquiler de prendas en stock

# Microservicio: autenticación de usuarios
para la realizacion de este microservicio se utilizo el framework django, con el lenguaje de programacion python, las pruebas correspondientes se realizaron en postman 

# Contenido de Este repositorio: 

 1. Se tiene una carpeta llamada auth_example donde donde se administran las aplicaciones que el proyecto este utiliza, esta carpeta contiene las carpetas: models, migrations, serializers y views, asi como los archivos admin.py, apps.py y test.py. 

 2. Se tiene una carpeta llamada backend_auth_tienda donde se guardan todas las configuraciones del servidor del componente, esta carpeta contiene los archivos: asgi.py, settings_dev.py, settings_prod.py, urls.py y wsgi.py. 

 3. se creo un archivo dockerfile el cual es un archivo de texto plano que contiene una serie de instrucciones necesarias para crear una imagen en un contenedor

 4. se tienen dos archivos que permiten iniciar un servidor web de manera local y en la nube, estos archivos son manage_dev.py y manage.py

 # Requerimientos 
```
  Django==3.2.9
  djangorestframework==3.12.4
  djangorestframework-simplejwt==5.0.0
  psycopg2-binary==2.9.1
  pyJWT==2.1.0
  gunicorn==20.1.0
  django-heroku==0.3.1
  drf-spectacular==0.21.0
```

# Ejecución del proyecto

para ejecutar el proyecto en local:

1. Se descarga el proyecto comprimido de GitHub

2. Al tener el proyecto en el ordenador, por la consola de comandos de ingresa al proyecto utilizando el comando cd:
   ```
    cd proyecto_p5Final
   ```
3. se debe inicializar el entorno virtual:

   ```
    env/Scripts/activate
   ```
4. se debe ingresar el siguiente comando para ejecutar el proyecto en local(computador personal o servidor):

   ```
    python manage_dev.py runserver 
   ```
El proyecto se encuentra en un contenedor docker en la plataforma heroku:

https://tienda-auth-ms-p5-g6.herokuapp.com/

# Pruebas

La ejecución de los casos de prueba se hizo por medio de la aplicacion postman:

https://go.postman.co/workspace/My-Workspace~e1b3bbc5-068f-4b94-81a3-673a8a8700d5/collection/17863004-dbc023ce-fc9a-419e-a86a-f0e405252c24