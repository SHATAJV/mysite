 


__________________________________________________________________________________________________
2.2.2
1-from polls.models import Question
questions = Question.objects.all()
for question in questions:
    print(f"ID: {question.id}, Texte: {question.question_text}, Date de publication: {question.pub_date}")
____________________________________________________________________________________________
2-from polls.models import Question
questions_octobre_2024 = Question.objects.filter(pub_date__year=2024, pub_date__month=10)

for question in questions_octobre_2024:
    print(f"ID: {question.id}, Texte: {question.question_text}, Date de publication: {question.pub_date}")
---------------------------------------------------------------------------------------------
3-from polls.models import Question
questions_id_2 = Question.objects.filter(id=2)
for question in questions_id_2:
    print(f"ID: {question.id}, Texte: {question.question_text}, Date de publication: {question.pub_date}")
--------------------------------------------------------------------------------------------
4- from polls.models import Question, Choice
questions = Question.objects.all()

for question in questions:
    print(f"Question: {question.question_text}, Date de publication: {question.pub_date}")
    choices = question.choice_set.all() 
    for choice in choices:
        print(f"  Choix: {choice.choice_text}, Votes: {choice.votes}")
---------------------------------------------------------------------------------------------
5- for question in questions:
      print(f"Question: {question.question_text}, Nombre de choix: {question.choice_set.count()}")
----------------------------------------------------------------------------------------------
7-questions = Question.objects.all().order_by('-pub_date')
for question in questions:
    print(f"Question: {question.question_text}, Date de publication: {question.pub_date}")
----------------------------------------------------------------------------------------------
9-from polls.models import Question, Choice
from django.utils import timezone
import datetime
new_question = Question(question_text="what is your favorite color ?", pub_date=timezone.now())
new_question.save()
_________________________________________________________________________________________
10-choice1 = Choice(question=new_question, choice_text="blue", votes=0)
choice1.save()
choice2 = Choice(question=new_question, choice_text="red", votes=3)
choice2.save()
choice3 = Choice(question=new_question, choice_text="purpel", votes=0)
choice3.save()
----------------------------------------------------------------------------
11-recent_questions = Question.objects.filter(pub_date__gte=timezone.now() - datetime.timedelta(days=1))

for question in recent_questions:
    print(f"Question: {question.question_text}, Date de publication: {question.pub_date}")
