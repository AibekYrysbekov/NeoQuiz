from django.contrib import admin
from .models import Category, Article, Quiz, Question, Answer

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
