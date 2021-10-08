from rest_framework import viewsets
from .serializer import CardSerializer
from insightApi.models import Card, Tag
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class CardSpecsViewSet(viewsets.ModelViewSet):
  serializer_class = CardSerializer
  queryset = Card.objects.all()
  permission_classes= IsAuthenticated,

  def retrieve(self, request, *args, **kwargs):
    params = kwargs

    tag = Tag.objects.filter(name=params['pk'])
    if not tag:
      return Response({'msg': 'Nenhum resultado disponível.'})
    cards = Card.objects.filter(tags = tag[0].id)
    serializer = CardSerializer(cards, many=True)

    return Response(serializer.data)


  def create(self, request, *args, **kwargs):
    card_data = request.data
    new_tag = None
    if(card_data["tag_name"] != ''):
      new_tag, created = Tag.objects.get_or_create(name=card_data["tag_name"])
    
    new_card = Card.objects.create(texto=card_data["texto"], tags=new_tag)
    new_card.save()

    serializer = CardSerializer(new_card)

    return Response(serializer.data)

  def update(self, request, *args, **kwargs):
    card_object = self.get_object()
    card_data = request.data

    new_tag = None
    if(card_data["tag_name"] != ''):
      new_tag, created = Tag.objects.get_or_create(name=card_data["tag_name"])

    card_object.texto = card_data["texto"]
    card_object.tags = new_tag
    card_object.save()

    serializer = CardSerializer(card_object)
    return Response(serializer.data)


  def destroy(self, request, pk=None):
    card = self.get_object()
    card.delete()
    return Response({"message": "Insight deletado com sucesso"})
  
  

  
    