# Generated by Django 4.1.3 on 2022-12-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funny', '0004_resume_delete_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]
