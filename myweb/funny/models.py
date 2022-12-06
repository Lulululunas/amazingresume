from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    
    first_name = models.CharField(max_length=50, help_text="First name")
    last_name = models.CharField(max_length=50, help_text="Last name")
    user_email = models.EmailField(max_length=120, help_text="Email")
    education = models.TextField(max_length=500, help_text="University")
    experience = models.TextField(max_length=500, help_text="Professional experience")
    skills = models.TextField(max_length=500, help_text="Skills")
    languages = models.CharField(max_length=300, help_text="Foreign languages")
    image = models.ImageField(default='default.jpg', upload_to='images')

    def get_absolute_url(self):

         return reverse('form-detail', args=[str(self.id)])

    def __str__(self):

        return self.user_email

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)