from django.db import models

class Calculation(models.Model):
    input = models.CharField(max_length=200)
    output = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.input + " = " + self.output


