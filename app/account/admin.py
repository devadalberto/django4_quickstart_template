from django.contrib import admin

from .models import Customer

admin.site.register(Customer)

# from django.contrib import admin
# from .models import User
# from .forms import UserCreationForm
# from django.contrib.auth.admin import UserAdmin


# class UserAdmin(UserAdmin):
#     model = User
#     add_form = UserCreationForm


# admin.site.register(User, UserAdmin)
