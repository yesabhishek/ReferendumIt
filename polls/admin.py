from django.contrib import admin
from .models import Petition,Agenda

class PetitionAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('id', 'agenda', 'choice', 'created_on', 'updated_on')
    list_filter = ('id', 'choice', 'created_on', 'updated_on')
    ordering = ('-id',)

class AgendaAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('id','status','agenda_text', 'ends_on', 'created_on', 'updated_on')
    list_filter = ('id', 'created_on', 'updated_on')
    ordering = ('-id',)


admin.site.register(Petition,PetitionAdmin)
admin.site.register(Agenda,AgendaAdmin)