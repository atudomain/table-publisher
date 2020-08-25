from django.urls import path

from . import views

app_name = 'tables'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:the_slug>/', views.DetailView.as_view(), name='detail')
]
