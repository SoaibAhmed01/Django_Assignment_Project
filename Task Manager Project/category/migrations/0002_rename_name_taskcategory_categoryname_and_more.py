# Generated by Django 4.2.7 on 2023-12-08 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskcategory',
            old_name='name',
            new_name='categoryName',
        ),
        migrations.RemoveField(
            model_name='taskcategory',
            name='tasks',
        ),
    ]
