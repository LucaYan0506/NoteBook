# Generated by Django 4.0.1 on 2022-01-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0006_alter_page_title_alter_subpage_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
