# Generated by Django 4.0.1 on 2022-01-12 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0004_alter_user_first_name_alter_user_middle_name_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled', max_length=200)),
                ('content', models.TextField()),
                ('poster', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='page', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled', max_length=200)),
                ('content', models.TextField()),
                ('parent_page', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='child', to='to_do_list.page')),
            ],
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
