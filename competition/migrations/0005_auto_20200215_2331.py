# Generated by Django 3.0.2 on 2020-02-15 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0004_auto_20200215_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amateurcompetition',
            old_name='Motivational Letter',
            new_name='letter',
        ),
        migrations.RenameField(
            model_name='amateurcompetition',
            old_name='Plot Description',
            new_name='plot',
        ),
        migrations.RenameField(
            model_name='amateurcompetition',
            old_name='Movie Poster',
            new_name='poster',
        ),
        migrations.RenameField(
            model_name='amateurcompetition',
            old_name='Movie Title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='amateurcompetition',
            name='Link to your movie',
        ),
        migrations.AddField(
            model_name='amateurcompetition',
            name='link',
            field=models.URLField(default='www.yourmovielink.com', max_length=128, unique=True),
        ),
    ]
