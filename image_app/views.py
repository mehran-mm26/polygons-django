import random
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ImageAnnotation
from django.shortcuts import render

class RandomImageView(APIView):
    def get(self, request):
        images = UploadedImage.objects.all()
        if images.exists():
            random_image = random.choice(images)
            serializer = UploadedImageSerializer(random_image)
            return Response(serializer.data)
        return Response({"error": "No images found."})

@csrf_exempt
def save_annotation(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            image_url = data.get("image")
            polygons = data.get("polygons")

            if not image_url or not polygons:
                return JsonResponse({"error": "Missing image or polygons"}, status=400)

            annotation = ImageAnnotation.objects.create(
                image_url=image_url,
                polygons=polygons
            )
            return JsonResponse({"message": "Saved successfully", "id": annotation.id})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid method"}, status=405)


def home_page(request):
    return render(request, 'index.html')
