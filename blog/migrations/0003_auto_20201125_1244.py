# Generated by Django 2.1 on 2020-11-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201125_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(default='www.hi.com', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='link2',
            field=models.URLField(default='www.hi.com', null=True),
        ),
    ]
