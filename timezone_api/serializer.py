from rest_framework import serializers

class TzSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=10)
    code = serializers.CharField(max_length=2)
