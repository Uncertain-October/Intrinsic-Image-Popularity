from django.db import models
from django import forms
# from django.core.files.uploadedfile import SimpleUploadedFile
import uuid
from typing import cast


# Create your models here.
class ImageRating(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    image = models.ImageField()
    url = models.URLField(default=str)
    rating_obj = models.JSONField(default=dict[str, float])
    rated_img_name = models.CharField(default=str)
    rated_value = models.FloatField(default=float)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ImageRatingForm(forms.ModelForm):
    class Meta:
        model = ImageRating
        fields = ["image"]

    def clean_image(self):
        image = self.cleaned_data.get("image", False)
        if image:
            if image.__sizeof__() > 15 * 1024 * 1024:
                raise forms.ValidationError("Image file too large ( > 15mb )")
            return image
        else:
            raise forms.ValidationError("Couldn't read uploaded image")
