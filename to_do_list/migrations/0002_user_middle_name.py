# Generated by Django 4.0.1 on 2022-01-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
