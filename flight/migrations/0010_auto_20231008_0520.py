# Generated by Django 3.1.2 on 2023-10-07 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0009_auto_20231008_0519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='training',
            old_name='course_edate_adate',
            new_name='course_edate',
        ),
    ]
