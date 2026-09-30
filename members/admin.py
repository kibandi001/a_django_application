from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Member
from .resources import MemberResource

@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    resource_classes = [MemberResource]

    list_display = (
        "membership_no",
        "full_name",
        "father_name",
        "grandfather_name",
        "email",
        "date_of_birth",
    )

    search_fields = ("membership_no", "full_name", "email")
    list_filter = ("date_of_birth",)
    ordering = ("membership_no",)