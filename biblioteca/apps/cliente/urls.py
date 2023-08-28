from django.urls import path
from .views import cliente
from .views import sobreNosotros

urlpatterns = [
    path('', cliente),
    path('sobreNosotros/', sobreNosotros)


]
