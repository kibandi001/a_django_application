from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "membership_no",
                    models.CharField(
                        help_text="Unique membership number, used to match rows on import.",
                        max_length=50,
                        unique=True,
                    ),
                ),
                ("full_name", models.CharField(max_length=255)),
                (
                    "father_name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="father's name"
                    ),
                ),
                (
                    "grandfather_name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="grandfather's name"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("date_of_birth", models.DateField()),
            ],
            options={
                "ordering": ["membership_no"],
            },
        ),
    ]
