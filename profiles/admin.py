from django.contrib import admin
from .models import Profile, Cursos
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extras', {
            'fields': ('curso', 'bio')
        }),
    )

'''
class ProfileCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile
        # Escreva a lista explicitamente (não esqueça do username, ele é obrigatório!)
        fields = ['username', 'email', 'curso', 'bio']
'''        

# 1. Registra o Profile customizado
admin.site.register(Profile, CustomUserAdmin)

# 2. Registra a tabela de Cursos para cadastrar
admin.site.register(Cursos)