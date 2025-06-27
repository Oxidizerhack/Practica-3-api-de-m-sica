from django.contrib import admin
from musica.models import Instrumentos, Ritmo, Departamento, Agrupacion, Cancion


# Register your models here.

admin.site.register(Instrumentos)
admin.site.register(Ritmo)
admin.site.register(Departamento)
admin.site.register(Agrupacion)
admin.site.register(Cancion)