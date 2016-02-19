from django.db import models


class Container(models.Model):
    name = models.CharField(max_length=50, help_text="Give the container a name to identify it")
    placement = models.CharField(max_length=150, help_text="Where is the container placed?")
    in_use = models.BooleanField(default=True, help_text="Is the container in use?")
    created = models.DateTimeField(auto_now_add=True)


class ContainerReading(models.Model):
    container = models.ForeignKey(Container)
    datetime = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()
