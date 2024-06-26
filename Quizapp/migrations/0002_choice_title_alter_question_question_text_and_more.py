# Generated by Django 5.0.3 on 2024-03-27 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
