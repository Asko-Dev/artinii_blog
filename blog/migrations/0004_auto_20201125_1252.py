# Generated by Django 2.1 on 2020-11-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201125_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image2',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='hi', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content2',
            field=models.TextField(default='hi', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content3',
            field=models.TextField(default='hi', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content4',
            field=models.TextField(default='hi', null=True),
        ),
    ]