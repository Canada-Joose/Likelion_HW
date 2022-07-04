from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    n_hit = models.PositiveIntegerField(default=0)


@property
def update_counter(self):
    self.n_hit = self.n_hit + 1
    self.save()
