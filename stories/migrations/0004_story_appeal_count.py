# Generated by Django 5.0.6 on 2024-06-22 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_remove_story_recipient_story_partner_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='appeal_count',
            field=models.IntegerField(default=0),
        ),
    ]
