# Generated by Django 4.0.4 on 2022-11-03 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('mes_codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('mes_preco', models.FloatField()),
                ('mes_local', models.CharField(max_length=270)),
                ('mes_quant_cadeiras', models.IntegerField()),
                ('mes_status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('emp_cnpj', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('emp_razao_social', models.CharField(max_length=50)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_senha', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cli_cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('cli_nome', models.CharField(max_length=50)),
                ('cli_email', models.EmailField(max_length=254)),
                ('cli_senha', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('alu_mes_codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('alu_mes_preco', models.FloatField()),
                ('alu_mes_quant_cadeiras', models.IntegerField()),
                ('alu_status', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]