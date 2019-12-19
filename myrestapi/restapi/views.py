from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import FindHotels
from .serializer import FindHotelsSerializers
from django.http import Http404


# class Hotellist(APIView):
#     def get(self,request):
#         hotel = FindHotels.objects.all()
#         serializer=FindHotelsSerializers(hotel,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = FindHotelsSerializers

class Hotellist(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return FindHotels.objects.get(pk=pk)
        except FindHotels.DoesNotExist:
            raise Http404

    def get(self, request,  *args, **kwargs):
        pk = self.kwargs.get('pk')
        snippet = self.get_object(pk)
        serializer = FindHotelsSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        snippet = self.get_object(pk)
        serializer = FindHotelsSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)