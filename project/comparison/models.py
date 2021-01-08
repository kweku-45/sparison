from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None , null= True)
    liked_songs = models.ManyToManyField("Song",  default=None,  related_name="users_that_liked_me")
    relationships = models.ManyToManyField('self', through='Relationship',
                                           symmetrical=False,
                                           related_name='related_to')
    class Meta:
        db_table = "UserProfile"

    def __str__(self):
        return self.user.username



RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)


    
class Album(models.Model):
    Album_name = models.CharField(max_length=40)  

    class Meta:
        db_table= "Album"

    def __str__(self):
        return self.Album_name

class Song(models.Model):
    track_name = models.CharField(max_length=250)
    artiste_name= models.CharField(
    max_length=200)
    album = models.ForeignKey(Album, on_delete= models.CASCADE, null=True, default=None, related_name = "songs")

    class Meta:
        db_table="Song"
    
    def __str__(self):
        return self.track_name


class Relationship(models.Model):
    from_person = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='from_people')
    to_person = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)



   
