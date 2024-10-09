from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('all/', views.AllPollsView.as_view(), name='all_polls'),
    path('<int:question_id>/frequency/', views.FrequencyView.as_view(), name='frequency'),
    path('statistics/', views.statistics_view, name='statistics'),
    path('create/', views.create_question, name='create_question'),
]