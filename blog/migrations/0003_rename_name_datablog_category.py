# Generated by Django 4.0.4 on 2022-05-26 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_datablog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datablog',
            old_name='name',
            new_name='category',
        ),
    ]
