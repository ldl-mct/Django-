# Generated by Django 3.2.7 on 2021-09-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_entermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entermodel',
            name='src',
        ),
        migrations.AlterField(
            model_name='entermodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]