from rest_framework.response import  Response
from rest_framework.views import APIView
from .models import  *
from .serializers import *

class AktyorlarAPI(APIView):
    def get(self, request):
        aktyorlar=Acter.objects.all()
        serializer=ActerSerializer(aktyorlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        aktyor=request.data
        serializer=ActerSerializer(data=aktyor)
        if serializer.is_valid():
            data=serializer.validated_data
            Acter.objects.create(
                name=data.get('name'),
                t_sana=data.get('t_sana'),
                davlat=data.get('davlat'),
                gender=data.get('gender'),
            )
            return Response({'success': True, 'created_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})

class Bitta_acterAPI(APIView):
    def get(self, request, pk):
        aktyor=Acter.objects.get(id=pk)
        serializer=ActerSerializer(aktyor)
        return Response(serializer.data)

    def put(self, request, pk):
        aktyor=Acter.objects.filter(id=pk)
        serializer=ActerSerializer(aktyor.first(), data=request.data)
        if serializer.is_valid():
            data=serializer.validated_data
            aktyor.update(
                name=data.get('name'),
                t_sana=data.get('t_sana'),
                davlat=data.get('davlat'),
                gender=data.get('gender'),
            )
            serializer=ActerSerializer(aktyor.first())
            return Response({'success': True, 'updated_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})

    def delete(self , request, pk):
        aktyor=Acter.objects.get(id=pk)
        aktyor.delete()
        return Response({'success': True})

class TariflarAPI(APIView):
    def get(self, request):
        tariflar=Tarif.objects.all()
        serializer=TariflarSerializer(tariflar, many=True)
        return Response(serializer.data)

    def post(self, request):
        tarif=request.data
        serializer=TariflarSerializer(data=tarif)
        if serializer.is_valid():
            data = serializer.validated_data
            Tarif.objects.create(
                nom=data.get('nom'),
                davomiyligi=data.get('davomiyligi'),
                narx=data.get('narx'),
            )
            return Response({'success': True, 'created_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})

class TarifAPI(APIView):
    def get(self, request, pk):
        tarif=Tarif.objects.get(id=pk)
        serializer=TariflarSerializer(tarif)
        return Response(serializer.data)

    def put(self, request, pk):
        tarif=Tarif.objects.filter(id=pk)
        serializer=TariflarSerializer(tarif.first(), data=request.data)
        if serializer.is_valid():
            data=serializer.validated_data
            tarif.update(
                nom=data.get('nom'),
                davomiyligi=data.get('davomiyligi'),
                narx=data.get('narx'),
            )
            serializer=TariflarSerializer(tarif.first())
            return Response({'success': True, 'updated_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})
    def delete(self , request, pk):
        tarif=Tarif.objects.get(id=pk)
        tarif.delete()
        return Response({'success': True})

