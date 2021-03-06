# Generated by Django 4.0.3 on 2022-03-20 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ammo',
            name='image',
        ),
        migrations.RemoveField(
            model_name='ranged',
            name='image',
        ),
        migrations.AddField(
            model_name='ammo',
            name='thumbnail',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='images/ammo'),
        ),
        migrations.AddField(
            model_name='ranged',
            name='thumbnail',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='images/ranged'),
        ),
    ]
