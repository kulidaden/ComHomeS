# Generated by Django 4.1.5 on 2023-03-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comhome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='number',
            field=models.IntegerField(default=380000000000, verbose_name='Номер телефону'),
        ),
    ]