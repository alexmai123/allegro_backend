from django import forms
from django.contrib import admin
from .models import Role, Event, Member
# Register your models here.


class MemberForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'active', 'email', 'phone', 'year', 'pro_pic', 'roles', 'section', 'staging')
        model = Member

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'staging')
    search_fields = ('name',)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'email', 'phone', 'year', 'section', 'staging')
    search_fields = ('employee__email', 'reporting_to__email')
    form = MemberForm


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'staging')
    search_fields = ('title', 'created')


admin.site.register(Role, RoleAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Event, EventAdmin)
