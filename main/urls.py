from django.urls import path
from .views import (CategoryListCreateView, ArticleListCreateView, QuizListCreateView, QuestionListCreateView,
                    AnswerListCreateView, ArticleSearchView, ArticleUpdateView)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('articles/', ArticleListCreateView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleUpdateView.as_view(), name='article-update'),
    path('quizzes/', QuizListCreateView.as_view(), name='quiz-list'),
    path('questions/', QuestionListCreateView.as_view(), name='question-list'),
    path('answers/', AnswerListCreateView.as_view(), name='answer-list'),
    path('categories/<int:category_id>/articles/', ArticleListCreateView.as_view(), name='category-articles'),
    path('articles/search/', ArticleSearchView.as_view(), name='article-search'),

]
