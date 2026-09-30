from import_export import fields, resources
from import_export.widgets import DateWidget

from .models import Member


class MemberResource(resources.ModelResource):
    """Maps Member model fields to the exact column headers you asked for:
    membership_no, full_name, father's_name, grandfather's_name, email,
    date-of-birth. These are what show up in every imported/exported file,
    regardless of the internal Python field names.
    """

    membership_no = fields.Field(attribute="membership_no", column_name="membership_no")
    full_name = fields.Field(attribute="full_name", column_name="full_name")
    father_name = fields.Field(attribute="father_name", column_name="father's_name")
    grandfather_name = fields.Field(
        attribute="grandfather_name", column_name="grandfather's_name"
    )
    email = fields.Field(attribute="email", column_name="email")
    date_of_birth = fields.Field(
        attribute="date_of_birth",
        column_name="date-of-birth",
        widget=DateWidget(format="%Y-%m-%d"),
    )

    class Meta:
        model = Member
        import_id_fields = ("membership_no",)
        fields = (
            "membership_no",
            "full_name",
            "father_name",
            "grandfather_name",
            "email",
            "date_of_birth",
        )
        export_order = fields
        skip_unchanged = True
        report_skipped = True
