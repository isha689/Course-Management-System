from rest_framework.views import exception_handler
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response:
        return response
    elif isinstance(exc, (IntegrityError, KeyError)):
        data = {'detail': str(exc) + ". Input data is Not Valid"}
        return Response(data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    elif isinstance(exc, ObjectDoesNotExist):
        data = {'detail': str(exc)}
        return Response(data, status=status.HTTP_404_NOT_FOUND)
