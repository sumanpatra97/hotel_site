# Generated by Django 3.0.1 on 2020-05-01 04:26

from django.db import migrations, models
import travel_app.file


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0006_auto_20200501_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourist',
            name='password',
            field=models.CharField(max_length=64, validators=[travel_app.file.new]),
        ),
    ]
