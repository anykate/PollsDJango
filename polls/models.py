from django.db import models
from django.db.models import Sum


# Create your models here.
class Poll(models.Model):
    poll = models.CharField(max_length=255)
    created_at = models.DateTimeField('Created on', auto_now_add=True)
    updated_at = models.DateTimeField('Updated on', auto_now=True)

    def total_votes(self):
        """Calculates the total number of votes for this poll"""
        return self.choices.aggregate(Sum('votes'))['votes__sum']

    def __str__(self):
        """Returns a string representation of this Poll"""
        return self.poll


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    choice = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField('Created on', auto_now_add=True)
    updated_at = models.DateTimeField('Updated on', auto_now=True)

    def votes_percentage(self):
        """Calculates the percentage of votes of this choice"""
        total = self.poll.total_votes()
        return self.votes / float(total) * 100 if total > 0 else 0

    def __str__(self):
        return self.choice
