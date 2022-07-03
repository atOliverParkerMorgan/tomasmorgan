from django.core.exceptions import ValidationError
from django.db import models


class BackgroundImages(models.Model):
    class Meta:
        verbose_name_plural = 'Background Images'

    def __str__(self):
        return "Background Images"


class BackgroundImage(models.Model):
    background_images = models.ForeignKey(BackgroundImages, null=True, related_name='background_image', on_delete=models.CASCADE)
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


class Songs(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    audio = models.FileField(upload_to='audio')
    cover_image = models.ImageField(
        upload_to='cover_images',
        height_field=None,
        width_field=None,
        max_length=None,
        default="/defaultbook.jpg"
    )

    def save(self, *args, **kwargs):
        if not self.pk and AboutMe.objects.exists():
            raise ValidationError('there can be only one Songs object')
        return super(Songs, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Songs'

    def __str__(self):
        return "Songs"


class Contact(models.Model):
    location = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()

    facebook_link = models.CharField(max_length=500, null=True, blank=True)
    instagram_link = models.CharField(max_length=500, null=True, blank=True)
    soundcloud_link = models.CharField(max_length=500, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.pk and AboutMe.objects.exists():
    #         raise ValidationError('there can be only one Contact object')
    #     return super(Contact, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Contact'

    def __str__(self):
        return "Contact"
