from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)  
    last_name = serializers.CharField(max_length=30)  
    mobile = serializers.CharField(max_length=10)  
    email = serializers.EmailField()  