# Generated by Django 3.2.7 on 2022-04-06 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_profisional_atividades_profissional'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividades',
            old_name='data_incio',
            new_name='data_inicio',
        ),
    ]
