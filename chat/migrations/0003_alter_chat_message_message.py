# Generated by Django 4.0.1 on 2022-02-13 17:53

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chat_group_created_time_chat_group_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_message',
            name='message',
            field=encrypted_model_fields.fields.EncryptedCharField(),
        ),
    ]
