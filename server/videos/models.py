from django.db import models


class KeyWord(models.Model):
    created_on = models.DateTimeField("Created on", auto_now_add=True)
    updated_on = models.DateTimeField("Updated on", auto_now=True)
    title = models.CharField("Title", max_length=255)
    description = models.TextField("Description")

    class Meta:
        verbose_name = "Key Word"
        verbose_name_plural = "Key Words"
        ordering = ['-created_on', 'title']

    def __str__(self):
        return self.title


class Video(models.Model):
    created_on = models.DateTimeField("Created on", auto_now_add=True)
    updated_on = models.DateTimeField("Updated on", auto_now=True)
    title = models.CharField("Title", max_length=255)
    link = models.URLField(
        "Video Link", max_length=255, help_text="The URL to the video page")
    key = models.CharField("Key", max_length=255)
    description = models.TextField("Description")

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ['-created_on', 'title']

    def __str__(self):
        return self.title
