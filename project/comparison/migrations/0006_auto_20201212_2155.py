# Generated by Django 3.1.3 on 2020-12-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0005_auto_20201212_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='liked_songs',
            field=models.ManyToManyField(default=None, null=True, related_name='users_that_liked_me', to='comparison.Song'),
        ),
    ]
