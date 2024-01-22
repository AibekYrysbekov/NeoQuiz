from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'study_time', 'image', 'date_created', 'backgroundColor', 'category']


class QuizSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Quiz
        fields = ['id', 'description', 'num_questions', 'image', 'date_created', 'backgroundColor', 'category']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
