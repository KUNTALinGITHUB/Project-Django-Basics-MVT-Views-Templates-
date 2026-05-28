from blog.models import Post
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Post)

admin.site.unregister(User)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email')

admin.site.register(User, CustomUserAdmin)


# create super user "python manage.py createsuperuser" with this custom admin 

# Username (leave blank to use 'kuntal'): kuntal
# Email address: kuntal7550@gmail.com
# Password: Kuntal@123
# Password (again): Kuntal@123
# The password is too similar to the username.
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.




# Django shows many fields:

# username
# email
# first name
# last name
# staff status
# etc.

# But your assignment wants only:

# username
# email