# Generated by Django 4.1.3 on 2022-12-05 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funny', '0006_alter_resume_education_alter_resume_experience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
