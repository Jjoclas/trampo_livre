# Generated by Django 3.2.7 on 2022-04-11 23:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=1000)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('horas_realizadas', models.IntegerField()),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=1000)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profissionais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=1000)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos')),
                ('cpf', models.CharField(max_length=11)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.setor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=1000)),
                ('nota', models.IntegerField()),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.atividades')),
            ],
        ),
        migrations.AddField(
            model_name='atividades',
            name='contratante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios'),
        ),
        migrations.AddField(
            model_name='atividades',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profissionais'),
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('repeticao', models.CharField(choices=[('diaria', 'diaria'), ('dias uteis', 'dia_util'), ('semanal', 'semanal'), ('mensal', 'mensal'), ('nunca', 'nunca')], max_length=10)),
                ('hora_inicio', models.TimeField(null=True)),
                ('hora_fim', models.TimeField(null=True)),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.atividades')),
            ],
        ),
    ]
