# Generated by Django 3.0.3 on 2020-02-15 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20200214_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecommendation',
            name='counselor_name',
            field=models.CharField(choices=[('1', 'Ms. Marino'), ('2', 'Mr. Robinson')], max_length=50),
        ),
    ]
