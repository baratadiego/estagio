from django.contrib import admin
from .models import Estagiario, Convenio, Estagio, Documento, Notificacao

# Register all models in admin site
admin.site.register(Estagiario)
admin.site.register(Convenio)
admin.site.register(Estagio)
admin.site.register(Documento)
admin.site.register(Notificacao)
