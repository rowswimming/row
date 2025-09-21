from django.db import models


class Opportunity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    points = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
        
    def __str__(self):
        return self.name
    

class Volunteer(models.Model):
    parent = models.ForeignKey('club.Parent', on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    application_date = models.DateField()
    application_accepted = models.BooleanField(default=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    points_earned = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.parent.user.first_name + ' ' + self.parent.user.last_name
