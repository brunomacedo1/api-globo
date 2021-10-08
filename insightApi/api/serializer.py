from rest_framework import serializers
from insightApi.models import Tag, Card

class CardSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Card
    fields = ['id', 'texto', 'tags', 'data_criacao', 'data_modificacao']
    depth = 1
  
 
    