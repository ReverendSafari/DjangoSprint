from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def like_count(self):
        return self.like_set.count()
      
class Like():
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      post = models.ForeignKey(Post, on_delete=models.CASCADE)
      
      class Meta:
         unique_together = ('user', 'post')