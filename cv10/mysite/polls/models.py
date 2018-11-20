from django.db import models

# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    count = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.question_text