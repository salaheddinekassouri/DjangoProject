from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    schedule_day = models.CharField(max_length=20, blank=True, null=True)
    schedule_time = models.TimeField(blank=True, null=True)
    students = models.JSONField(default=list, blank=True)  # store student IDs from Spring Boot microservice

    def __str__(self):
        return self.name
