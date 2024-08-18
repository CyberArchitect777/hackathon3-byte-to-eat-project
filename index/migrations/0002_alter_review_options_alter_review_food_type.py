# Generated by Django 4.2.15 on 2024-08-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_on'], 'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.AlterField(
            model_name='review',
            name='food_type',
            field=models.CharField(choices=[('Indian', 'Indian'), ('Italian', 'Italian'), ('Chinese', 'Chinese'), ('Thai', 'Thai'), ('Japanese', 'Japanese'), ('Mexican', 'Mexican'), ('British', 'British'), ('French', 'French'), ('Greek', 'Greek'), ('American', 'American'), ('Turkish', 'Turkish'), ('Korean', 'Korean'), ('Vietnamese', 'Vietnamese'), ('Spanish', 'Spanish'), ('Lebanese', 'Lebanese'), ('Caribbean', 'Caribbean'), ('Other', 'Other')], default='Indian', max_length=20),
        ),
    ]
