# Generated by Django 4.0.1 on 2022-01-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_picture_height_alter_picture_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='width',
            field=models.IntegerField(),
        ),
    ]
