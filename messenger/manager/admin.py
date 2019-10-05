from django.contrib import admin
#importar todos los modelos
from .models import *

#Registrar modelos
admin.site.register(category)      #registrar un sitio -->crea administrador de sitio en el servidor
admin.site.register(author)
admin.site.register(contact)
admin.site.register(post)
admin.site.register(suscriber)
admin.site.register(web)
admin.site.register(social)