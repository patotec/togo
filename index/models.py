from django.db import models

# Create your models here.
class email(models.Model):
    subject = models.CharField(max_length=50)
    file = models.CharField(max_length=5000)
    html_file = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject