# Generated by Django 3.0.3 on 2020-02-15 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200215_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='data_published',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
