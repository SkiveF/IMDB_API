from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from moviesdata.models import MoviesData
from moviesdata.serializers import MoviesdataSerializer
from rest_framework.decorators import api_view
import pandas as pd
import json

@api_view(['GET', 'POST', 'DELETE'])
def movies_list(request):
    
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    movies = MoviesData.objects.all()
    movies_serializer = MoviesdataSerializer(movies, many=True)

    return JsonResponse(movies_serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def movies_category(request):
    

    movies_df = pd.DataFrame(list(MoviesData.objects.all().values()))

    title_type = movies_df.groupby('Category').agg('count')

    data = []
    for index,row in title_type.iterrows():
        data.append([index, row['Rank']])

    #movies_serializer = MoviesdataSerializer(json.loads(data), many=True)
    
    data_df = pd.DataFrame(data, columns=["Category","Number"])
    data_json = data_df.to_json(orient='records')
    
    data_json = json.loads(data_json)


    return JsonResponse(data_json, safe=False)
    
@api_view(['GET', 'PUT', 'DELETE'])
def movies_gross(request):
    

    movies_df = pd.DataFrame(list(MoviesData.objects.all().values()))

    Top_10_Gross = movies_df[movies_df.Gross != -1]
    Top_10_Gross = Top_10_Gross.sort_values(['Gross'],ascending=False).head(10)
    
    
    data_json = Top_10_Gross.to_json(orient='records')
    
    data_json = json.loads(data_json)


    return JsonResponse(data_json, safe=False)
   

@api_view(['GET', 'PUT', 'DELETE'])
def movies_rating(request):
    

    movies_df = pd.DataFrame(list(MoviesData.objects.all().values()))

    Top_10_best_rated = movies_df.sort_values(['Rating'],ascending=False).head(10)
    
    
    data_json = Top_10_best_rated.to_json(orient='records')
    
    data_json = json.loads(data_json)


    return JsonResponse(data_json, safe=False)
    
        

@api_view(['GET', 'PUT', 'DELETE'])
def movies_duration(request):
    

    movies_df = pd.DataFrame(list(MoviesData.objects.all().values()))

    Top_10_longest = movies_df.sort_values(['Duration'],ascending=False).head(10)
    
    data_json = Top_10_longest.to_json(orient='records')
    
    data_json = json.loads(data_json)


    return JsonResponse(data_json, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def movies_most_rated(request):
    

    movies_df = pd.DataFrame(list(MoviesData.objects.all().values()))

    Top_10_most_noted = movies_df.sort_values(['Votes_number'],ascending=False).head(10)
    
    data_json = Top_10_most_noted.to_json(orient='records')
    
    data_json = json.loads(data_json)


    return JsonResponse(data_json, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def movies_top_metascore(request):
    

    movies_df = pd.DataFrame(list(MoviesData.objects.all().values()))

    Top_10_best_metascore = movies_df[movies_df.Metascore != -1]
    Top_10_best_metascore = Top_10_best_metascore.sort_values(['Metascore'],ascending=False).head(10)
    
    data_json = Top_10_best_metascore.to_json(orient='records')
    
    data_json = json.loads(data_json)


    return JsonResponse(data_json, safe=False)