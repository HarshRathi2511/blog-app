# Generated by Django 3.2.9 on 2021-11-30 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='datePosted',
            new_name='date_posted',
        ),
    ]
