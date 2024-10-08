 


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