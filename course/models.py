from django.db import models


class Validator(models.Manager):
    def validate(self, form_data):
        errors = {}
        for key, value in form_data.items():
            if key == "name" and len(value) <= 5:
                errors[key] = "Course name must be more than 5 characters."
            elif key == "desc" and len(value) <= 15:
                errors[key] = "Description must be more than 15 characters."
        return errors


class Course(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validator()
