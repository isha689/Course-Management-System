from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CourseModel
from .serializers import CourseSerializer
from rest_framework import serializers, status
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List all Courses' : '/list',
        'Search courses by title' : '/list?title=A',
        'Search courses by course ID' : '/list?id=1',
        'Create a Course' : '/create',
        'Update a Course' : '/update/{courseID}',
        'Delete a Course' : '/delete/{courseID}'
    }
    return Response(api_urls)


@api_view(['POST'])
def CreateCourse(request):
    course = CourseSerializer(data=request.data)

    if CourseModel.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if course.is_valid():
        course.save()
        return Response(course.data, status = status.HTTP_201_CREATED)
    else:
        return Response("Invalid Format.", status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ListCourse(request):

    if request.query_params:
        courses = CourseModel.objects.filter(**request.query_params.dict())
    else:
        courses = CourseModel.objects.all()
 
    if courses:
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    else:
        return Response("Requested Data doesn't exist in database.", status = status.HTTP_404_NOT_FOUND)
    

@api_view(['PUT'])
def UpdateCourse(request,pk):
    course = get_object_or_404(CourseModel, pk=pk)
    course = CourseSerializer(instance=course, data=request.data, partial=True)
    
    if course.is_valid():
        course.save()
        return Response(course.data, status = status.HTTP_202_ACCEPTED)
    else:
        return Response("Invalid Format.", status = status.HTTP_400_BAD_REQUEST)

   
@api_view(['DELETE'])
def DeleteCourse(request,pk):
    course = get_object_or_404(CourseModel, pk=pk)
    course.delete()
    return Response("Successfully deleted", status = status.HTTP_200_OK)
