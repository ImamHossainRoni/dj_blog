
from django.urls import path
from blog import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_details, name='post_details'),
]
