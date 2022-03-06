from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from crud.models import Person

from crud.serializers import PersonSerializer

class RetrievePersonsAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        person_list = Person.objects.all()
        serializer = PersonSerializer(person_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreatePersonAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDeletePersonAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, person_id):
        person_obj = get_object_or_404(Person, pk=person_id)
        serializer = PersonSerializer(person_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, person_id):
        person_obj = get_object_or_404(Person, pk=person_id)
        serializer = PersonSerializer(instance=person_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, person_id):
        person_obj = get_object_or_404(Person, pk=person_id)
        person_obj.status = False
        person_obj.save()
        return Response({'message':'Elininado'}, status=status.HTTP_204_NO_CONTENT)