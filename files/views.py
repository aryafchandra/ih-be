# files/views.py
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import CSV
from .serializers import CSVSerializer
import csv

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_csv(request):
    file = request.FILES.get('file')
    name = request.data.get('name', file.name)

    csv_record = CSV.objects.create(name=name, file=file)
    serializer = CSVSerializer(csv_record)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_csv_data(request, file_id):
    try:
        csv_record = CSV.objects.get(pk=file_id)
    except CSV.DoesNotExist:
        return Response({'error': 'File not found'}, status=404)

    with open(csv_record.file.path, newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    return Response(data, status=200)
