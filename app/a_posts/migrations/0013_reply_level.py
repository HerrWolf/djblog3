# Generated by Django 4.2 on 2024-11-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0012_reply_parent_reply_alter_reply_parent_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
