# Generated by Django 4.2 on 2024-09-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0004_alter_tag_options_tag_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='icons/'),
        ),
    ]
