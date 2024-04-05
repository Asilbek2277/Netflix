from rest_framework import serializers

class ActerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    t_sana = serializers.DateField()
    davlat = serializers.CharField(max_length=50)
    gender = serializers.CharField(max_length=10)


class TariflarSerializer(serializers.Serializer):
    nom = serializers.CharField(max_length=200)
    davomiyligi = serializers.CharField(max_length=10)
    narx = serializers.IntegerField()