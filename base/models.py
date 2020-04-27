from django.db import models

class Todo(models.Model):
    image = models.ImageField(blank = True, upload_to="")
    name = models.CharField(max_length = 255)
    want = models.CharField(max_length = 500)
    where = models.CharField(max_length = 500)

    def __str__(self):
        return self.name+self.want[0:40]