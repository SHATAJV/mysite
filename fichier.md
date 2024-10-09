
## 1. Admin.py

```python
admin.site.register(Choice)
```

## 2. Image
## 3.OUI     

## 4. Class QuestionAdmin

```python
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('pub_date',)
    ordering = ('pub_date',)
    search_fields = ('question_text',)

admin.site.register(Question, QuestionAdmin)
```

### (5-7): Oui

__________________________________________________________________________________________________

## 2.2.2

### 1. Fetch all questions:

```python
from polls.models import Question
questions = Question.objects.all()

for question in questions:
    print(f"ID: {question.id}, Texte: {question.question_text}, Date de publication: {question.pub_date}")
```

____________________________________________________________________________________________

### 2. Fetch questions from October 2024:

```python
from polls.models import Question
questions_octobre_2024 = Question.objects.filter(pub_date__year=2024, pub_date__month=10)

for question in questions_octobre_2024:
    print(f"ID: {question.id}, Texte: {question.question_text}, Date de publication: {question.pub_date}")
```
![un image result](images/question2_1.png)
---------------------------------------------------------------------------------------------

### 3. Fetch question with ID = 2:

```python
from polls.models import Question
questions_id_2 = Question.objects.filter(id=2)

for question in questions_id_2:
    print(f"ID: {question.id}, Texte: {question.question_text}, Date de publication: {question.pub_date}")
```

--------------------------------------------------------------------------------------------

### 4. Fetch questions with their choices:

```python
from polls.models import Question, Choice
questions = Question.objects.all()

for question in questions:
    print(f"Question: {question.question_text}, Date de publication: {question.pub_date}")
    choices = question.choice_set.all()
    for choice in choices:
        print(f"  Choix: {choice.choice_text}, Votes: {choice.votes}")
```
![un image result](images/question2_3.png)
---------------------------------------------------------------------------------------------

### 5. Fetch questions and the number of choices:

```python
for question in questions:
    print(f"Question: {question.question_text}, Nombre de choix: {question.choice_set.count()}")
```

--------------------------------------------------------------------------------------------

### 7. Fetch all questions ordered by publication date:

```python
questions = Question.objects.all().order_by('-pub_date')

for question in questions:
    print(f"Question: {question.question_text}, Date de publication: {question.pub_date}")
```
![un image result](images/question2_5.png)
---------------------------------------------------------------------------------------------

### 9. Create a new question:

```python
from polls.models import Question, Choice
from django.utils import timezone
import datetime

new_question = Question(question_text="what is your favorite color ?", pub_date=timezone.now())
new_question.save()
```

_________________________________________________________________________________________

### 10. Create choices for the new question:

```python
choice1 = Choice(question=new_question, choice_text="blue", votes=0)
choice1.save()

choice2 = Choice(question=new_question, choice_text="red", votes=3)
choice2.save()

choice3 = Choice(question=new_question, choice_text="purple", votes=0)
choice3.save()
```

----------------------------------------------------------------------------

### 11. Fetch recent questions:

```python
recent_questions = Question.objects.filter(pub_date__gte=timezone.now() - datetime.timedelta(days=1))

for question in recent_questions:
    print(f"Question: {question.question_text}, Date de publication: {question.pub_date}")
```

_____________________________________________________________________________________________

## 3.1: Index.html

```html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a>
<small>Publié le : {{ question.pub_date }}</small></li>
```

![un image result](images/question_3_1.png)


-------------------------------------------------------

## 3.2: In polls/views.py

```python
class AllPollsView(generic.ListView):
    template_name = 'polls/all_polls.html'
    context_object_name = 'all_questions'

    def get_queryset(self):
        '''Retourne tous les sondages classés par date de publication'''
        return Question.objects.order_by("-pub_date")
```

## In urls.py:

```python
path('all/', views.AllPollsView.as_view(), name='all_polls'),
```

Create an HTML file:

```html
<h1>Liste de tous les sondages</h1>

{% if all_questions %}
    <ul>
    {% for question in all_questions %}
        <li>
            Sondage ID: {{ question.id }} -
            <a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a>
            <small>(Publié le : {{ question.pub_date }})</small>
        </li>
    {% endfor %}
    </ul>
{% else %}
    <p>Aucun sondage disponible.</p>
{% endif %}
```

![un image result](images/question_3_2.png)

---------------------------------------------------------------------------------

## 3.3: In views.py:

```python
class FrequencyView(generic.DetailView):
    model = Question
    template_name = "polls/frequency.html"
    pk_url_kwarg = 'question_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        context['choices'] = question.get_choices()
        return context
```

## In urls.py:

```python

 path('<int:question_id>/frequency/', views.FrequencyView.as_view(), name='frequency'),
 
```
##  In frequency.html:


```html
<h1>Résultats du sondage : {{ question.question_text }}</h1>

<ul>
    {% for choice, votes, percent in choices %}
        <li>{{ choice.choice_text }} - {{ votes }} ({{ percent }}%)</li>
    {% endfor %}
</ul>

```
# modifiy all_polls.html: 

```html
 <a href="{% url 'frequency' question.id %}">{{ question.question_text }}</a>
```
## In models.py (class question): 
```python

        def get_choices(self):
        choices = self.choice_set.all()
        total_votes = sum(choice.votes for choice in choices)
        results = []
        for choice in choices:
            votes = choice.votes
            percent = (votes / total_votes * 100) if total_votes > 0 else 0
            results.append((choice, votes, percent))
        return results
```
![un image result](images/question3_3png.png)
---------------------------------------------------------------------------------------
