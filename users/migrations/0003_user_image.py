# Generated by Django 5.0.3 on 2024-04-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=1, upload_to='student'),
            preserve_default=False,
        ),
    ]
