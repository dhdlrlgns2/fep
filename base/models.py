from django.db import models
from django.utils import timezone

class Todo(models.Model):
    image = models.ImageField(blank = False,null = False, upload_to="")
    name = models.CharField(max_length = 255)
    want = models.CharField(max_length = 500)
    where = models.CharField(max_length = 500)
    updated_at = models.DateTimeField(default=timezone.now)
    imgur = models.TextField(max_length = 100)

    def __str__(self):
        return self.name+"["+self.want[0:40]+"] ("+str(self.updated_at)[0:16]+")"