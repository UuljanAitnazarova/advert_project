# Generated by Django 3.2.6 on 2021-08-21 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('ad', 'ad'), ('announcement', 'announcement')], max_length=13)),
                ('description', models.TextField(max_length=400)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advert', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
