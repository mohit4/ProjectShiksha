# Generated by Django 3.1 on 2021-04-21 17:36

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
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('video_link', models.URLField(max_length=500)),
                ('content_files', models.FileField(max_length=500, upload_to='uploads/')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]