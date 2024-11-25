Me permito entregarle el proyecto asignado, no obstante, debo informar que el mismo está incompleto debido a algunos problemas técnicos que encontré durante su desarrollo.

A continuación, detallo las principales dificultades enfrentadas:

1) Conexión con la base de datos:
    Inicialmente, intenté conectar el proyecto a una base de datos PostgreSQL, pero esto generaba problemas que impedían que el servidor funcionara correctamente. Para avanzar en el desarrollo, decidí cambiar a la base de datos predeterminada de Django, lo que permitió restablecer la funcionalidad básica del servidor.

2)Problemas en las URLs del proyecto:
    Al iniciar el servidor, me fue imposible visualizar las páginas correctamente debido a errores en la configuración de las URLs. Trabajé en resolver este inconveniente, pero no logré solucionarlo por completo, lo que resultó en un error que detalla lo siguiente:
"Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\Usuario\Bootcamp-Ecom24\entornos\ve_litoralpay\Lib\site-packages\django\urls\resolvers.py", line 720, in url_patterns
    iter(patterns)
TypeError: 'module' object is not iterable

...

django.core.exceptions.ImproperlyConfigured: The included URLconf '<module 'transactions.urls' from 'C:\\Users\\Usuario\\Bootcamp-Ecom24\\src\\transactions\\urls.py'>' does not appear to have any patterns in it. If you see the 'urlpatterns' variable with valid patterns in the file then the issue is probably caused by a circular import."

Este error parece estar relacionado con un problema en el archivo transactions/urls.py, posiblemente debido a una importación circular o una configuración incorrecta del objeto urlpatterns.

A pesar de mis esfuerzos, no pude corregir este inconveniente antes de la fecha de entrega.


