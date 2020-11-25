from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from moviesdata.models import MoviesData
from moviesdata.serializers import MoviesdataSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def movies_list(request):
    
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    movies = MoviesData.objects.all()
    movies_serializer = MoviesdataSerializer(movies, many=True)

    return JsonResponse(movies_serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    
        

