# Generated by Django 4.0.1 on 2022-02-03 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0020_remove_chat_message_chat_group_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='pk_folder',
        ),
    ]
