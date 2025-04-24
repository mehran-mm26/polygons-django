from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class UploadedImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/', storage=MediaCloudinaryStorage())

    def __str__(self):
        return self.title
