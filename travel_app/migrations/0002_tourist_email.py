# Generated by Django 3.0.1 on 2020-04-21 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourist',
            name='email',
            field=models.EmailField(default='test@example.com', max_length=254),
        ),
    ]
