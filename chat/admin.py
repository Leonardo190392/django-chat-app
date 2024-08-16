from .models import Message, Chat
from django.contrib import admin

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat','text', 'created_at', 'author', 'receiver') # zeigt die genannten sachen im einzelnen object an
    list_display = ('text', 'created_at', 'author', 'receiver') # zeigt die genannten Sachen im Overlay(Chat) an
    search_fields = ('text',) # so kann man nach text suchen/filtern

# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
