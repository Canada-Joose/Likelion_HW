from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    n_hit = models.PositiveIntegerField(default=0)


@property
def update_counter(self):
    self.n_hit = self.n_hit + 1
    self.save()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return self.content
