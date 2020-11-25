from django.conf.urls import url 
from moviesdata import views 
 
urlpatterns = [ 
    url(r'^api/movies$', views.movies_list),
]
