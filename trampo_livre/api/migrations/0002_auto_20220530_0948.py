# Generated by Django 3.2.7 on 2022-05-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='data_fim',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='data_inicio',
            field=models.DateField(),
        ),
    ]