# Generated by Django 2.0.3 on 2019-10-16 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Personal_Information',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
