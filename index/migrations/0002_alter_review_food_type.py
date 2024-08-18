# Generated by Django 4.2.15 on 2024-08-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='food_type',
            field=models.IntegerField(choices=[(0, 'Indian'), (1, 'Italian'), (2, 'Chinese'), (3, 'Thai'), (4, 'Japanese'), (5, 'Mexican'), (6, 'British'), (7, 'French'), (8, 'Greek'), (9, 'American'), (10, 'Turkish'), (11, 'Korean'), (12, 'Vietnamese'), (13, 'Spanish'), (14, 'Lebanese'), (15, 'Caribbean'), (16, 'Other')], default=0),
        ),
    ]
