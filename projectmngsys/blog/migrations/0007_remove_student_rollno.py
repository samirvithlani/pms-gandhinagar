# Generated by Django 4.1.4 on 2023-01-09 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_question_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='rollno',
        ),
    ]