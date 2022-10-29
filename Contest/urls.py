from django.urls import path
from . import views
urlpatterns = [
    path('contest/<str:id>', views.contest, name='contest'),
    path('create/', views.create, name='create'),
    path('caesar/', views.caesar, name="caesar"),
    path('list/', views.listContest, name='list'),
    path('list/<str:id>', views.listContestQuestions, name='listQuestions'),
    path('', views.index, name="index"),
]
