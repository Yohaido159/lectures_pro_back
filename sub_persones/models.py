from django.db import models



class SubPerson(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=254, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
