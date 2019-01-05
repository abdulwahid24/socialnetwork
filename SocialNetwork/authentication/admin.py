from django.contrib import admin

from authentication.models import User, Profile


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    exclude = ('user', )


admin.site.register(User)
admin.site.register(Profile, ProfileAdmin)
