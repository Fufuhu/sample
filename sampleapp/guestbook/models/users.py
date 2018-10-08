from django.db import models
import uuid

class Commentator(models.Model):
    commentator_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, default='名無しさん', blank=False, unique=True)