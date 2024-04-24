from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework import status
from school_app.models import *
from school_app.serializers import *
# Create your views here.

#GET
@api_view(['GET'])    ##school list
def school_list(request):
    if request.method == 'GET':
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
#POST
  
@api_view(['GET', 'POST'])      ##school add
def school_add(request): 
    if request.method == 'GET':
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def school_view(request, school_id):     ##school view
    schools = School.objects.get(id=school_id)
    if request.method ==  'GET':
        serializer = SchoolSerializer(schools)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET', 'DELETE'])
def school_delete(request, school_id):      ##school delete
    schools = School.objects.get(id=school_id)
    if request.method ==  'GET':
        serializer = SchoolSerializer(schools)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        schools.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def batch_list(request):   ##batch list
    if request.method == 'GET':
        batch = Batch.objects.all()
        serializer = BatchSerializer(batch, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET', 'POST'])
def batch_add(request):       ##batch add
    if request.method == 'GET':
        batch = Batch.objects.all()
        serializer = BatchSerializer(batch, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def batch_view(request, batch_id):      ##batch view
    batch = Batch.objects.get(id=batch_id)
    if request.method ==  'GET':
        serializer = BatchSerializer(batch)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET', 'DELETE'])
def batch_delete(request, batch_id):           ##batch delete
    batch = Batch.objects.get(id=batch_id)
    if request.method ==  'GET':
        serializer = BatchSerializer(batch)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        batch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def student_list(request):            ##student list
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET', 'POST'])
def student_add(request):          ##student add
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def student_view(request, student_id):               ##student view
    student = Student.objects.get(id=student_id)
    if request.method ==  'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET', 'DELETE'])
def student_delete(request, student_id):              ##student delete
    student = Student.objects.get(id=student_id)
    if request.method ==  'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
    
    
## PUT AND PATCH

@api_view(['GET', 'PATCH'])     ##PATCH
def school_edit1(request, school_id):
    try:
        schools = School.objects.get(id=school_id)
    except School.DoesNotExist:
        return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SchoolSerializer(schools)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = SchoolSerializer(schools, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT'])      ##PUT
def school_edit2(request, school_id):
    try:
        schools = School.objects.get(id=school_id)
    except School.DoesNotExist:
        return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SchoolSerializer(schools)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        serializer = SchoolSerializer(schools, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])     ##PATCH
def batch_edit1(request, batch_id):
    try:
        batch = Batch.objects.get(id=batch_id)
    except Batch.DoesNotExist:
        return Response({'error': 'Batch not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BatchSerializer(batch)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = BatchSerializer(batch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
   

@api_view(['GET', 'PUT'])      ##PUT
def batch_edit2(request, batch_id):
    try:
        batch = Batch.objects.get(id=batch_id)
    except Batch.DoesNotExist:
        return Response({'error': 'Batch not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BatchSerializer(batch)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        serializer = BatchSerializer(batch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
##  USING CLASS

class StudentEdit1(APIView):
    def get(self, request, student_id, format=None):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, student_id, format=None):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentEdit2(APIView):
    def get(self, request, student_id, format=None):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, student_id, format=None):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
## BATCH WITHIN SCHOOL

class StudentWithBatch(APIView):
    def get(self, request, student_id, format=None):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        student_serializer = StudentSerializer(student)
        batch = Batch.objects.filter(student=student)
        batch_serializer = BatchSerializer(batch, many=True)

        

        response_data = {
            'student': student_serializer.data,
            'batch': batch_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)
    
    
class SchoolWithBatch(APIView):
    def get(self ,request,school_id):
        try:
            schools = School.objects.get(id=school_id)
        except School.DoesNotExist:
            return Response({'error': 'school not found '}, status=status.HTTP_404_NOT_FOUND)
        
        school_serializer = SchoolSerializer(schools)
        batch = Batch.objects.filter(school=schools)
        
        final_data=[]
        
        for batch in batch:
            batch_serializer = BatchSerializer(batch)
            student = Student.objects.filter(batch=batch)
            student_serializer = StudentSerializer(student, many=True)
            
            batch_data = batch_serializer.data
            batch_data['variants'] = student_serializer.data
            
            final_data.append(batch_data)


        response_data ={
            'school': school_serializer.data,
            'batch' : final_data
            
        }

        return Response(response_data,status=status.HTTP_200_OK)