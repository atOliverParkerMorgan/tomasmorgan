from django.core.exceptions import ValidationError
from django.db import models


class BackgroundImages(models.Model):
    class Meta:
        verbose_name_plural = 'Background Images'

    def __str__(self):
        return "Background Images"


class BackgroundImage(models.Model):
    background_images = models.ForeignKey(BackgroundImages, null=True, related_name='background_image',
                                          on_delete=models.CASCADE)
    background_image = models.ImageField(
        upload_to='cover_images',
        height_field=None,
        width_field=None,
        max_length=None,
        default="/defaultbook.jpg"
    )


class AboutMe(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and AboutMe.objects.exists():
            raise ValidationError('there can be only one About me object')
        return super(AboutMe, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'About me'

    def __str__(self):
        return "About me"


class Subtitle(models.Model):
    subtitles = models.ForeignKey(AboutMe, null=True, related_name='text', on_delete=models.CASCADE)
    text = models.CharField(max_length=50, null=True, blank=True)


class Album(models.Model):
    album_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.album_name


class Gallery(models.Model):
    gallery_image = models.ImageField(
        upload_to='cover_images',
        height_field=None,
        width_field=None,
        max_length=None,
        default=None,
    )
    description = models.CharField(default="", max_length=30)


class Song(models.Model):
    name_of_song_album = models.ForeignKey(Album, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True, blank=True)

    audio = models.FileField(upload_to='audio')
    cover_image = models.ImageField(
        upload_to='cover_images',
        height_field=None,
        width_field=None,
        max_length=None,
        default="/defaultbook.jpg"
    )

    class Meta:
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.name


class Contact(models.Model):
    location = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()

    facebook_link = models.CharField(max_length=500, null=True, blank=True)
    instagram_link = models.CharField(max_length=500, null=True, blank=True)
    soundcloud_link = models.CharField(max_length=500, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and AboutMe.objects.exists():
            raise ValidationError('there can be only one Contact object')
        return super(Contact, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Contact'

    def __str__(self):
        return "Contact"
