from rest_framework import serializers
from .models import *

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        

        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
        
class BatchSerializer(serializers.ModelSerializer):
    # school_name = serializers.SerializerMethodField()
    
    school = SchoolSerializer()
   
    class Meta:
        model = Batch
        fields = ['name', 'year', 'school']
        
    # def get_school_name(self, obj):
    #     return obj.school.name if obj.school else None