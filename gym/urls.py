from django.urls import path
from . import views
from .tasks import page


urlpatterns = [
    path('', views.home_clients, name='home'),
    path('perm/', views.AddEvent.as_view(), name='add_event'),
    path('page/', page, name='page')
]