from django.urls import path

from .views      import ListKeyword,DetailKeyword, home
# from .views      import 

urlpatterns = [
    path('apis/v1/'         , ListKeyword  .as_view()),
    path('apis/v1/<int:pk>/', DetailKeyword.as_view()),
    #path(''                 , home())
]
