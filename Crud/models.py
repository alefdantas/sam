
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Cliente (models.Model):
    cli_cpf = models.CharField(max_length=11,primary_key=True)
    cli_nome = models.CharField(max_length=50)
    cli_email = models.EmailField()
    cli_senha = models.CharField(max_length=20)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
class Empresa(models.Model):
    emp_cnpj = models.CharField(max_length=14,primary_key=True)
    emp_razao_social = models.CharField(max_length=50)
    emp_email = models.EmailField()
    emp_senha = models.CharField(max_length=20)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)


class Mesa(models.Model):
    mes_codigo = models.IntegerField(primary_key=True)
    mes_preco = models.FloatField()
    mes_local = models.CharField(max_length=270)
    mes_quant_cadeiras = models.IntegerField()
    mes_status = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

class Aluguel(models.Model):
    alu_mes_codigo = models.IntegerField(primary_key=True)
    alu_mes_preco = models.FloatField()
    alu_mes_quant_cadeiras = models.IntegerField()
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
