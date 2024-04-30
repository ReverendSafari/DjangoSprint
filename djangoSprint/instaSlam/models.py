from django.db import models
from django.contrib.auth.models import User

#Model for posts with a counter method to count likes
class Post(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def like_count(self):
        return self.like_set.count()

#Model for likes, has a unique_together field to insure user can only like a post once   
class Like(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      post = models.ForeignKey(Post, on_delete=models.CASCADE)
      
      class Meta:
         unique_together = ('user', 'post')