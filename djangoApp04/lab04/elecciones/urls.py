from django.urls import URLPattern, path

from . import views

app_name = 'elecciones'
urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:region_id>/', views.list_candidatos, name='list_candidatos'),
]