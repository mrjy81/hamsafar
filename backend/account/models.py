from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf.urls.static import static


class Users(AbstractUser):
    class Meta:
        verbose_name_plural = 'تمامی کاربران'


class Phones(models.Model):
    phone = models.CharField(_("شماره تلفن"), max_length=10, unique=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name_plural = 'تلفن ها'


class DriverModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            type='Driver'
        )


class ClientModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            type='Client'
        )


USER_TYPES = (('Driver', 'راننده'), ('Client', 'کاربر'))


class Driver(models.Model):
    GENDER = (('MALE', "مرد"), ("FEMALE", 'زن'))
    user = models.OneToOneField(Users, verbose_name=_(
        "کاربر"), on_delete=models.CASCADE)
    history = models.CharField(_("سابقه"), max_length=50, default='بدون سابقه')
    phone = models.ForeignKey(Phones, verbose_name=_(
        "شماره تلفن"), on_delete=models.PROTECT, related_name='driver_phone')
    rate = models.PositiveIntegerField(_("رتبه"), default=0)
    gender = models.CharField(_("جنسیت"), max_length=50, choices=GENDER)
    image = models.ImageField(
        _("تصویر"), upload_to='imgs', null=True, blank=True)
    type = models.CharField(_("نوع کاربر"), max_length=50,
                            choices=USER_TYPES, default='Driver')
    charge = models.PositiveIntegerField(verbose_name=_('اعتبار'),null=True , blank=True , default = 0)
    objects = DriverModelManager()

    class Meta:
        verbose_name_plural = 'رانندگان'

    def save(self, *args, **kwargs):
        if not self.image:
            if self.gender == 'MALE':
                self.image = 'imgs/boy.png'
            else:
                self.image = 'imgs/girl.png'

        return super(Driver, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Client(Driver):
    objects = ClientModelManager()

    def save(self, *args, **kwargs):
        self.type = 'Client'
        return super(Driver, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name_plural = 'کاربران'

# @receiver(post_save, sender=Driver)
# def image_handler(sender, instance, created, **kwargs):
#     if created:
#         if not instance.image:
#             if instance.gender == 'MALE':
#                 instance.image = 'boy.png'
#             else:
#                 instance.image = 'girl.png'
