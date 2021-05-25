from datetime import time, timezone

from django.db import models

STATUS_CHOICES = [
    ('n', 'Not posted'),
    ('p', 'Posted'),
]

class Mto(models.Model):
    microtask = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.microtask)


class MalRequirements(models.Model):
    # title = models.CharField(max_length=200)
    # date = models.DateField()
    # start_time = models.TimeField(default=time(9))
    # choices = models.ForeignKey(Mto, on_delete=models.CASCADE, related_name= 'microtask')
    name_of_microtask = models.ForeignKey(Mto, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return str(self.name_of_microtask)
