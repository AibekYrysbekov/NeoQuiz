# Generated by Django 5.0.1 on 2024-01-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='backgroundColor',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='backgroundColor',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
