# Generated by Django 3.2.2 on 2021-05-08 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0009_auto_20171115_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clip',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='memento',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
