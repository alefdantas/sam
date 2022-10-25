from pyexpat import model
from django.contrib import admin
from .models import Aluguel,Cliente,Empresa,Mesa

# Register your models here.
#class Admin(admin.ModelAdmin):
#    readonly_fields = ('mes_emp_cnpj', )
#    def save_model(self, request,obj, form,change):
#        usuario = request.GET.get('emp_cnpj')
#       obj.mes_emp_cnpj = usuario
        
#       return super(AdminMesa,self).save_model(request, obj, form, change)

admin.site.register(Mesa)
admin.site.register(Aluguel)
admin.site.register(Cliente)
admin.site.register(Empresa)

