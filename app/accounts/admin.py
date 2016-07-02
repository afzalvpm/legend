from django.contrib import admin
from django.contrib.auth.models import Group
from app.accounts.models import Account

admin.site.unregister(Group)
admin.site.register(Account)