from django.db import models

# Create your models here.


class GeneralSetting(models.Model):
    name = models.CharField(
        default="",
        max_length=255,
        blank=True,
        verbose_name="Name",
        help_text="Name of setting",)
    description = models.CharField(
        default="",
        max_length=255,
        blank=True,
        verbose_name="Description",
    )
    parameters = models.CharField(
        default="",
        max_length=255,
        blank=True,
        verbose_name="Parameters",
    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Updated Date",
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Created Date",
    )

    def __str__(self):
        return f'General setting: {self.name}'

    class Meta:
        verbose_name = "General Setting"
        verbose_name_plural = "General Settings"
        ordering = ('name',)

class ImageSetting(models.Model):
    name = models.CharField(
        default="",
        max_length=255,
        blank=True,
        verbose_name="Name",
        help_text="Name of setting", )
    description = models.CharField(
        default="",
        max_length=255,
        blank=True,
        verbose_name="Description",
    )
    file = models.ImageField(
        default="",
        verbose_name="Image",
        help_text="",
        blank=True,
        upload_to="images/",
    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Updated Date",
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Created Date",
    )

    def __str__(self):
        return f'Image setting: {self.name}'

    class Meta:
        verbose_name = "Image Setting"
        verbose_name_plural = "Image Settings"
        ordering = ('name',)
