from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None , null= True)
    liked_songs = models.ManyToManyField("Song", null=True , default=None,  related_name="users_that_liked_me")
    class Meta:
        db_table = "UserProfile"

    def __str__(self):
<<<<<<< HEAD
        

    

# def create_profile(sender, **kwargs):
#     if kwargs["created"]:
#         UserProfile = UserProfile.objects.create(user=kwargs["instance"])
 
# post_save.connect(create_profile, sender=User)
    
=======
        return self.user.first_name

    
>>>>>>> b54d9c04 (slight changes)
class Album(models.Model):
    Album_name = models.CharField(max_length=40)  

    class Meta:
        db_table= "Album"

    def __str__(self):
        return self.Album_name

class Song(models.Model):
    track_name = models.CharField(max_length=250)
    artiste_name= models.CharField(
<<<<<<< HEAD
     max_length=200)
=======
    max_length=200)
>>>>>>> b54d9c04 (slight changes)
    album = models.ForeignKey(Album, on_delete= models.CASCADE, null=True, default=None, related_name = "songs")

    class Meta:
        db_table="Song"
    
    def __str__(self):
        return self.track_name