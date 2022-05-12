from django.urls import path
from api import views

urlpatterns = [
    path('todo/', views.TodoAPIView.as_view()),
    path('todo/<int:pk>/', views.TodoAPIView.as_view()),
    path('agora/', views.agora.as_view(), name='agora'),
    path('imagedetect/', views.imagedetect.as_view(), name='image-detect'),

]