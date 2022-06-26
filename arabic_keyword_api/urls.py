from turtle import home
from django.urls import path

from .views      import HomePage, ListKeyword,DetailKeyword

app_name="arabic_t"
urlpatterns = [
    path('apis/v1/'         , ListKeyword  .as_view()),
    path('apis/v1/<int:pk>/', DetailKeyword.as_view()),
    path(''                 , HomePage.homy          ),
]
