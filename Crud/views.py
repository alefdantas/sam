from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Aluguel, Cliente, Empresa, Mesa
from django.contrib.auth import logout as django_logout


def index(request):
    return render(request,'index.html')

#  CRUD EMPRESA
#CRIAR EMPRESA
def create_empresa(request):
    if request.method == "GET":
        return render(request,'cadastroemp.html')
    else:
        emp_cnpj = request.POST.get('emp_cnpj')
        emp_razao_social = request.POST.get('emp_razao')
        emp_email = request.POST.get('emp_email')
        emp_senha = request.POST.get('emp_senha')
        user = User.objects.create_user(username=emp_razao_social,email=emp_email,id=emp_cnpj,password=emp_senha)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        user_aux = User.objects.get(id=user.id)
        new = Empresa(emp_cnpj=emp_cnpj,emp_razao_social=emp_razao_social,emp_email=emp_email,emp_senha=emp_senha,user=user_aux)
        
        new.save()
        return redirect('logar_empresa')

#CRIAR MESA
@login_required(login_url='/logar_empresa/')
def create_mesa(request):
    if request.method == "GET":
        return render(request,'cadasmesa.html')
    else:    
        mes_codigo = request.POST.get('mes_codigo')
        mes_quant_cadeiras = request.POST.get('mes_quant_cadeiras')
        mes_preco= request.POST.get('mes_preco')
        mes_local= request.POST.get('mes_local')
        new = Mesa(mes_codigo=mes_codigo,mes_quant_cadeiras=mes_quant_cadeiras,mes_local=mes_local,mes_preco=mes_preco,user=request.user)
        new.save()
        return redirect('admin_mesas')

@login_required(login_url='/logar_empresa/')
def delete_mesas(request,mes_codigo):
    mesa = Mesa.objects.get(mes_codigo=mes_codigo)
    mesa.delete()
    return redirect('admin_mesas')

@login_required(login_url='/logar_empresa/')
def update_mesas(request,mes_codigo):
    if request.method == 'GET':
        mesa = Mesa.objects.filter(mes_codigo=mes_codigo)
        return render (request,'updatemesa.html', {"mesa":mesa})
    else:
        mesa = Mesa.objects.get(mes_codigo=mes_codigo)
        mes_codigo = request.POST.get('mes_codigo')
        mes_quant_cadeiras = request.POST.get('mes_quant_cadeiras')
        mes_preco = request.POST.get('mes_preco')
        mes_local = request.POST.get('mes_local')
        new = new = Mesa(mes_codigo=mes_codigo,mes_quant_cadeiras=mes_quant_cadeiras,mes_local=mes_local,mes_preco=mes_preco,user=request.user)
        new.save()
        mesa.delete()
        return redirect('admin_mesas')
#ALTERA O STATUS DA MESA PARA ALUGADA
@login_required(login_url='/logar_cliente/')
def alugar(request,mes_codigo):
    mesa = Mesa.objects.get(mes_codigo=mes_codigo)
    mesa.mes_status = True
    mesa.save()
    user = request.user
    user_aux = User.objects.get(id=user.id)
    new = Aluguel(alu_status=mesa.mes_status,alu_mes_codigo=mesa.mes_codigo,alu_mes_preco=mesa.mes_preco,alu_mes_quant_cadeiras=mesa.mes_quant_cadeiras,user=user_aux)
    new.save()
    return redirect('lista_alugadas')

@login_required(login_url='/logar_cliente/')
def lista_alugadas(request):
    user = request.user
    aluguel = Aluguel.objects.filter(user=user)
    return render(request,'mesasalugadas.html',{"mesa_aux":aluguel})

#AREA DE ADMIN DAS MESAS DAS EMPRESAS
@login_required(login_url='/logar_empresa/')
def admin_mesas(request):
    user = request.user
    mesas = Mesa.objects.filter(user=user)
    return render(request,'mesas.html',{"mesas":mesas})

@login_required(login_url='/logar_empresa/')
def admin_mesas_alugadas(request):
    usuario = request.user
    mesa = Mesa.objects.filter(user=usuario)
    aluguel = Aluguel.objects.filter(alu_status=True)
    return render(request,'adminalugadas.html',{"mesas":mesa,"aluguel":aluguel})


#CRIAR CLIENTE
def create_cliente(request):
    if request.method == "GET":
        return render(request,'cadastrocli.html')
    else:
        cli_cpf = request.POST.get('cli_cpf')
        cli_nome = request.POST.get('cli_nome')
        cli_email = request.POST.get('cli_email')
        cli_senha = request.POST.get('cli_senha')
        user = User.objects.create_user(username=cli_nome,email=cli_email,password=cli_senha)
        user.is_superuser = False
        user.is_staff = False
        user.save()
        user_aux = User.objects.get(id=user.id)
        new = Cliente(cli_cpf=cli_cpf,cli_nome=cli_nome,cli_email=cli_email,cli_senha=cli_senha,user=user_aux)
        new.save()
        return redirect('logar_cliente')
        
#LOGAR COMO CLIENTE
def logar_cliente(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        clie_username = request.POST.get('cli_username')
        clie_senha = request.POST.get('cli_senha')
        usuario = authenticate(username=clie_username, password=clie_senha)
        if usuario:
            login(request,usuario)
            return redirect('aluguel_mesa_disponiveis')
        else:
            return redirect('logar_cliente')

#LOGAR COMO EMPRESA
def logar_empresa(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        cli_username = request.POST.get('cli_username')
        cli_senha = request.POST.get('cli_senha')
        usuario = authenticate(username=cli_username, password=cli_senha)
        if usuario:
            login(request,usuario)
            return redirect('admin_mesas')
        else:
            return redirect('logar_empresa')


#EXIBE TELA DE MESAS DISPONIVEIS PARA ALUGAR
@login_required(login_url='/logar_cliente/')
def aluguel_mesa_disponiveis(request):
    mesa = Mesa.objects.filter(mes_status=False)  
    return render(request,'aluguel.html',{"aluguel":mesa})

#LOGOUT DO CLIENTE
@login_required
def logout_cliente(request):
    django_logout(request)
    return redirect('logar_cliente')

#LOGOUT DA EMPRESA
@login_required
def logout_empresa(request):
    django_logout(request)
    return redirect('logar_empresa')
