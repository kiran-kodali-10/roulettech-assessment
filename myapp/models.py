from django.db import models
import json

class Person(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    position_title = models.CharField(max_length=100)
    description_points = models.TextField()  # Store JSON as string
    description = models.TextField()

    def set_description_points(self, x):
        self.description_points = json.dumps(x)

    def get_description_points(self):
        return json.loads(self.description_points)

    def __str__(self):
        return self.company_name
