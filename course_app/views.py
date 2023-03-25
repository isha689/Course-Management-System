from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CourseModel
from .serializers import CourseSerializer
from rest_framework import serializers, status
from .exception_handler import api_exception_handler
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List all Courses': '/list',
        'Search courses by title': '/list?title=A',
        'Search courses by course ID': '/list?id=1',
        'Create a Course': '/create',
        'Update a Course': '/update/{courseID}',
        'Delete a Course': '/delete/{courseID}'
    }
    return Response(api_urls)


@api_view(['POST'])
def create_course(request):
    course = CourseSerializer(data=request.data)

    if CourseModel.objects.filter(name=request.data['name']).exists():
        raise serializers.ValidationError('This data already exists')

    course.is_valid(raise_exception=True)
    course.save()
    return Response(course.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_course(request):

    if request.query_params:
        courses = CourseModel.objects.filter(
            **request.query_params.dict())
    else:
        courses = CourseModel.objects.all()

    if courses.exists():
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    return Response("Requested Data Not Found.", status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_course(request, pk):
    course = CourseModel.objects.get(pk=pk)
    course = CourseSerializer(instance=course, data=request.data, partial=True)

    course.is_valid(raise_exception=True)
    course.save()
    return Response(course.data, status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE'])
def delete_course(request, pk):
    course = CourseModel.objects.get(pk=pk)
    course.delete()
    return Response("Successfully deleted")
