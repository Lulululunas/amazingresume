# Generated by Django 4.1.3 on 2022-12-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funny', '0002_alter_form_education_alter_form_experience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
