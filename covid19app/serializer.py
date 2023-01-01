from rest_framework import serializers

class CountryNameSerializer(serializers.Serializer):
    name = serializers.CharField()