from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime
from django.db.models import Sum

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return "{} {} ".format(self.pub_date, self.question_text)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def age(self):

        return timezone.now() - self.pub_date

    def get_choices(self):
        choices = self.choice_set.all()
        total_votes = sum(choice.votes for choice in choices)
        results = []
        for choice in choices:
            votes = choice.votes
            percent = (votes / total_votes * 100) if total_votes > 0 else 0
            results.append((choice, votes, percent))
        return results

    @classmethod
    def total_questions(cls):

        return cls.objects.count()

    @classmethod
    def total_choices(cls):

        return sum(choice.choice_set.count() for choice in cls.objects.all())

    @classmethod
    def total_votes(cls):

        return sum(choice.votes for question in cls.objects.prefetch_related('choice_set').all() for choice in
                   question.choice_set.all())

    @classmethod
    def average_votes(cls):

        total_votes = cls.total_votes()
        total_questions = cls.total_questions()
        return total_votes / total_questions if total_questions > 0 else 0

    @classmethod
    def most_popular(cls):

        return cls.objects.annotate(total_votes=Sum('choice__votes')).order_by('-total_votes').first()

    @classmethod
    def least_popular(cls):

        return cls.objects.annotate(total_votes=Sum('choice__votes')).order_by('total_votes').first()

    @classmethod
    def latest_question(cls):

        return cls.objects.latest('pub_date')



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text