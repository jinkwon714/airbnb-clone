from django.contrib import admin
from django.contrib.auth.models import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fielsets = UserAdmin.fielsets + (
        "Custom Profile",
        {
            "fields": (
                "avatar",
                "gender",
                "bio",
                "birthday",
                "language",
                "currency",
                "superhost",
            )
        },
    )
