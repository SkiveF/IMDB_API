from django.conf.urls import url 
from moviesdata import views 
 
urlpatterns = [ 
    url(r'^api/movies$', views.movies_list),
    url(r'^api/movies/category$', views.movies_category),
    url(r'^api/movies/gross$', views.movies_gross),
    url(r'^api/movies/rating$', views.movies_rating),
    url(r'^api/movies/metascore$', views.movies_top_metascore),
    url(r'^api/movies/duration$', views.movies_duration),
    url(r'^api/movies/mostrated$', views.movies_most_rated),
]
