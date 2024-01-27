from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    # Name field
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    # State field with 2-character max string
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    # Primary key ID field
    id = models.IntegerField(primary_key=True, null=False)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Display name, state, and ID
        display_course = '{0.name}, {0.state}, {0.id}'
        return display_course.format(self)

    class Meta:
        # Define name to display
        verbose_name_plural = "University Campus"
