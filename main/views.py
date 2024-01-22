from django.db.models import Q
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Category, Article, Quiz, Question, Answer
from .serializers import CategorySerializer, ArticleSerializer, QuizSerializer, QuestionSerializer, AnswerSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CustomArticlePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ArticleListCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    pagination_class = CustomArticlePagination

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            queryset = Article.objects.filter(category_id=category_id)
        else:
            queryset = Article.objects.all()
        return queryset


class ArticleUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerListCreateView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ArticleSearchView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    pagination_class = CustomArticlePagination

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')

        if search_query:
            queryset = Article.objects.filter(Q(title__icontains=search_query))
        else:
            queryset = Article.objects.none()

        return queryset
