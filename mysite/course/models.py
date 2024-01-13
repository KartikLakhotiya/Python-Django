from django.db import models

# Create your models here.
class CourseName(models.Model):
    courseTitle= models.CharField(max_length = 50)
    coursePrice = models.IntegerField()
    courseHeading = models.CharField(max_length = 100)
    courseDesc = models.TextField()
    trainerName = models.CharField(max_length = 50)
    presentStudent = models.IntegerField()
    studentLikes = models.IntegerField()
    
    def __str__(self):
        return self.courseTitle
    
#hello
#hello again
    
    