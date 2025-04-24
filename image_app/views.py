import random
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UploadedImage
from .serializers import UploadedImageSerializer

class RandomImageView(APIView):
    def get(self, request):
        images = UploadedImage.objects.all()
        if images.exists():
            random_image = random.choice(images)
            serializer = UploadedImageSerializer(random_image)
            return Response(serializer.data)
        return Response({"error": "No images found."})
