from django.db import models
from embed_video.fields import EmbedVideoField
from django.urls import reverse
from django.utils import timezone


class Room(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    video = EmbedVideoField()
    publish = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('living_room:room_detail', args=[self.publish.year, self.publish.month,
                                                 self.publish.day, self.slug])
