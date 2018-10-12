#from django.urls import include, path
from django.conf.urls import include, url


from . import views

urlpatterns = [
    url(r'^', views.ListTodo.as_view()),
    url(r'^<int:pk>/', views.DetailTodo.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
]