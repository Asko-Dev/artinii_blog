# Generated by Django 2.1 on 2020-11-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201125_1422'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='blog_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(null=True, upload_to='blog_pics'),
        ),
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
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title3',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
