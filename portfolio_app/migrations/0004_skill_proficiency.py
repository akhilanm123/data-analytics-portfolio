# Generated by Django 5.1.7 on 2025-03-30 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='proficiency',
            field=models.CharField(default='Intermediate', max_length=50),
        ),
    ]
