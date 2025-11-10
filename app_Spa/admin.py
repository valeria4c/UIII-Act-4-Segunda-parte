# app_Spa/admin.py
from django.contrib import admin
from .models import Usuarios, Pedidos, Reseñas # Importa todos los modelos

# Registra el modelo Usuarios
admin.site.register(Usuarios)
admin.site.register(Pedidos)

# # Deja Pedidos y Reseñas pendientes por ahora
# admin.site.register(Pedidos)
# admin.site.register(Reseñas)python