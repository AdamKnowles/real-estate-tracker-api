from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from realestateapi.models import Property
from datetime import datetime
from datetime import date


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        url = serializers.HyperlinkedIdentityField(
            view_name='properties',
            lookup_field='id'
        )
        fields = ('id', 'title', 'address', 'year_built', 'price', 'square_feet', 'bedroom_count', 'bathroom_count', 'has_basement', 'date_listed', 'days_listed', 'price_per_square_foot', 'price_with_commas')

class Properties(ViewSet):

    def create(self, request):

       new_property = Property()
       new_property.title = request.data['title']
       new_property.address = request.data['address']
       new_property.year_built = request.data['year_built']
       new_property.price = request.data['price']
       new_property.square_feet = request.data['square_feet']
       new_property.bedroom_count = request.data['bedroom_count']
       new_property.bathroom_count = request.data['bathroom_count']
       new_property.has_basement = request.data['has_basement']
       new_property.date_listed = request.data['date_listed']
       new_property.save()

       serializer = PropertySerializer(new_property, context={'request': request})

       return Response(serializer.data)


    def retrieve(self, request, pk=None):
        
        try:
            
            property = Property.objects.get(pk=pk)
            serializer = PropertySerializer(property, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def list(self, request):
        

    
        properties = Property.objects.all()
        
        serializer = PropertySerializer(
            properties, many=True, context={'request': request})
        return Response(serializer.data)