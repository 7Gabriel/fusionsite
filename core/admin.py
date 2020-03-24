from django.contrib import admin

from .models import Cargo, Servico, Equipe, FeatureLeft, FeatureRight


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo','ativo','modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','icone','ativo','modificado')


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado', 'ativo')


@admin.register(FeatureLeft)
class FeatureLeftAdmin(admin.ModelAdmin):
    list_display = ('feature', 'modificado', 'ativo')


@admin.register(FeatureRight)
class FeatureRightAdmin(admin.ModelAdmin):
    list_display = ('feature', 'modificado', 'ativo')