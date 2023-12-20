# Generated by Django 4.1 on 2023-10-30 05:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Duration",
            fields=[
                (
                    "event_day",
                    models.DateField(
                        default=datetime.date.today, primary_key=True, serialize=False
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventDuration",
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
                    "duration",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="post.duration"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Favorite",
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
            ],
        ),
        migrations.CreateModel(
            name="Like",
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
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=30)),
                ("content", models.CharField(max_length=1000, null=True)),
                ("place", models.CharField(max_length=30, null=True)),
                ("image", models.ImageField(null=True, upload_to="images/")),
                ("is_festival", models.BooleanField(null=True)),
                ("like_count", models.IntegerField(default=0)),
                ("favorite_count", models.IntegerField(default=0)),
                ("time", models.CharField(max_length=100, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "event_durations",
                    models.ManyToManyField(
                        blank=True,
                        related_name="duration_events",
                        through="post.EventDuration",
                        to="post.duration",
                    ),
                ),
                (
                    "favorite_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="favorite_posts",
                        through="post.Favorite",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "like_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="like_posts",
                        through="post.Like",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="like",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="post.post"
            ),
        ),
        migrations.AddField(
            model_name="like",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="favorite",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="post.post"
            ),
        ),
        migrations.AddField(
            model_name="favorite",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="eventduration",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="post.post"
            ),
        ),
    ]