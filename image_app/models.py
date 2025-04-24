from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class UploadedImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/', storage=MediaCloudinaryStorage())

    def __str__(self):
        return self.title
    
class ImageAnnotation(models.Model):
    image_url = models.URLField()
    polygons = models.JSONField()  # Stores list of polygons (as JSON)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Annotation for {self.image_url}"
