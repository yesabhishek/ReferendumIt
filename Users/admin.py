from django.contrib import admin
from .models import Profile
admin.site.site_header = "Admin"
admin.site.site_title = "R Admin Portal"
admin.site.index_title = "Welcome to R Admin"


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('id', 'name', 'uid', 'mobile','t_and_c')
    list_filter = ('name', 'id', 't_and_c')
    ordering = ('-id',)

admin.site.register(Profile,ProfileAdmin)