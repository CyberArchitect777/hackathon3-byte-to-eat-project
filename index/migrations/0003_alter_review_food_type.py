# Generated by Django 4.2.15 on 2024-08-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_remove_review_approved_review_food_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='food_type',
            field=models.IntegerField(choices=[(0, 'Chinese'), (1, 'Curry'), (2, 'Pizza'), (3, 'Sushi'), (4, 'Burgers'), (5, 'Fish & Chips'), (6, 'Other')], default=0),
        ),
    ]
