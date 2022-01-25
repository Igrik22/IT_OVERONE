from django.http import JsonResponse
from rest_framework.decorators import api_view
from core.serializers import PictureSerializer


@api_view(['POST'])
def resize_picture(request):
    if request.method == 'POST':
        serializer = PictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data.get('uploaded_picture'), status=201, safe=False)
        return JsonResponse(serializer.errors)
