
from django.urls import path
from blog import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_details, name='post_details'),
]
