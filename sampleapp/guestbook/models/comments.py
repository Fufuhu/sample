from django.db import models
import uuid

from .users import Commentator

class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, blank=False)
    comment = models.TextField(blank=False)
    commentator = models.ForeignKey(to=Commentator, on_delete=models.CASCADE, blank=True)
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='oyako', null=True)
    append_at = models.DateTimeField(auto_now_add=True)