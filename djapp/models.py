from django.db import models

# Create your models here.


class Track (models.Model):
    track_name = models.CharField(max_length=50)

    def __str__(self):
        return self.track_name


class Student(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    student_track = models.ForeignKey(Track, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name+" "+self.last_name

    def is_adult(self):
        if (self.age > 25):
            return True
        else:
            return False

    is_adult.short_description = "Graduated Student"
    is_adult.boolean = True
