# Generated by Django 2.2 on 2019-05-07 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0006_auto_20190401_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absencemodel',
            name='time',
        ),
        migrations.AddField(
            model_name='absencemodel',
            name='lessons_skipped',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
