# Generated by Django 3.2.6 on 2021-08-21 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0003_advert_moderated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={'permissions': [('сan_approve', 'Can approve')]},
        ),
    ]