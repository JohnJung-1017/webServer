# Generated by Django 4.1.5 on 2023-05-23 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20200507_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='modify_count',
            field=models.IntegerField(default=0),
        ),
    ]