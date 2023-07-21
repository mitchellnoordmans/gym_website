from django.db import models
from datetime import timedelta


# Create your models here.

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    email = models.EmailField()
    phone_nr = models.CharField(max_length=20, null=True)
    personal_trainer = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    pricing = models.IntegerField()
    duration = models.DurationField(default=timedelta(days=30))

    def __str__(self):
        return self.name
    
class GroupLessons(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
        schedule = models.CharField(max_length=50)
        duration = models.DurationField()
        
        def _str__(self):
            return self.name
        
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ContactForm(models.Model):
    email = models.EmailField()
    question = models.TextField()

    def __str__(self):
        return self.email
