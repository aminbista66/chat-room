# Generated by Django 5.0.4 on 2024-05-04 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_conversation_tags_conversation_tag_delete_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
