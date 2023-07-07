from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}. {self.title} - {self.status}'
