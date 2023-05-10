from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from  embed_video.fields  import  EmbedVideoField

#Create your models here.
class  tutorial(models.Model):
	tutorial_Title = models.CharField(max_length=200)
	tutorial_Body = models.TextField()
	tutorial_Video = EmbedVideoField()

	class  Meta:
		verbose_name_plural = "Tutorial"

	def  __str__(self):
		return  str(self.tutorial_Title) if  self.tutorial_Title  else  " "


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
