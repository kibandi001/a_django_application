from django.db import models


class Member(models.Model):
    """A single membership record.

    membership_no is the natural key: import matches existing rows on it,
    so re-importing an updated file updates records instead of duplicating
    them.
    """

    membership_no = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique membership number, used to match rows on import.",
    )
    full_name = models.CharField(max_length=255)
    father_name = models.CharField("father's name", max_length=255, blank=True)
    grandfather_name = models.CharField("grandfather's name", max_length=255, blank=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()

    class Meta:
        ordering = ["membership_no"]

    def __str__(self) -> str:
        return f"{self.membership_no} — {self.full_name}"
