# Generated by Django 4.0.6 on 2022-07-18 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexslider',
            name='index_css',
        ),
        migrations.RemoveField(
            model_name='indexslider',
            name='index_text',
        ),
        migrations.RemoveField(
            model_name='indexslider',
            name='index_title',
        ),
    ]