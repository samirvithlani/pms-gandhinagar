# Generated by Django 4.1.4 on 2023-01-29 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
