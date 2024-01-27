from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    id = models.IntegerField(primary_key=True, null=False)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        display_course = '{0.name}, {0.state}, {0.id}'
        return display_course.format(self)

    class Meta:
        verbose_name_plural = "University Campus"
