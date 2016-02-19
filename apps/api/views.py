from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apps.api.models import ContainerReading
from apps.api.serializers import ContainerReadingModelSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def container_reading_list(request):
    """
    List all reading or create a new one
    """

    if request.method == 'GET':
        readings = ContainerReading.objects.all()
        serializer = ContainerReadingModelSerializer(readings, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContainerReadingModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        return JSONResponse(serializer.errors, status=400)
