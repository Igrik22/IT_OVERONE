# Generated by Django 4.0.1 on 2022-01-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_picture_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='uploaded_picture',
            field=models.ImageField(unique=True, upload_to='media/'),
        ),
    ]