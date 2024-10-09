from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


    def get_choices(self):
        choices = self.choice_set.all()
        total_votes = sum(choice.votes for choice in choices)
        results = []
        for choice in choices:
            votes = choice.votes
            percent = (votes / total_votes * 100) if total_votes > 0 else 0
            results.append((choice, votes, percent))
        return results


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text