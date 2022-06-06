from django.urls import path

from .views      import ListKeyword
from .views      import DetailKeyword

urlpatterns = [
    path(''         , ListKeyword  .as_view()),
    path('<int:pk>/', DetailKeyword.as_view())
]
