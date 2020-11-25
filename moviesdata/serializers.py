from rest_framework import serializers 
from moviesdata.models import MoviesData
 
 
class MoviesdataSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = MoviesData
        fields = ('id',
                  'Rank',
                  'Title',
                  'Rating',
                  'Metascore',
                  'Duration',
                  'Year',
                  'Category',
                  'Gross',
                  'Votes_number',
                  'Image')

