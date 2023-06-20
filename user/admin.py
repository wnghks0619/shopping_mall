from django.contrib import admin
from user.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email',) # 마지막에 , 안 넣으면 문자열로 인식해요.

admin.site.register(User, UserAdmin)