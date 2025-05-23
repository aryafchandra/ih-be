# Generated by Django 4.2.21 on 2025-05-21 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("dashboards", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Visualization",
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
                ("title", models.CharField(max_length=100)),
                (
                    "chart_type",
                    models.CharField(
                        choices=[
                            ("bar", "Bar Chart"),
                            ("line", "Line Chart"),
                            ("pie", "Pie Chart"),
                            ("scatter", "Scatter Plot"),
                        ],
                        max_length=20,
                    ),
                ),
                ("x_column", models.CharField(max_length=100)),
                ("y_column", models.CharField(max_length=100)),
                ("config", models.JSONField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "dashboard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="visualizations",
                        to="dashboards.dashboard",
                    ),
                ),
            ],
        ),
    ]
