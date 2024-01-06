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
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = Article.objects.filter(category_id=category_id)
        else:
            queryset = Article.objects.all()
        return queryset


class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerListCreateView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
