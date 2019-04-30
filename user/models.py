from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

from datetime import datetime, timedelta
import re
import os
def userImage_directory_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return 'profile/'+re.sub('[-:. ]','',str(datetime.today()))+file_extension

class User(AbstractBaseUser, PermissionsMixin):
    platformArray=(
        ('android',('android')),
        ('ios',('ios')),
    )
    profile_photo = models.ImageField(upload_to=userImage_directory_path,null=True,blank=True)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'),max_length = 50, unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    platform= models.CharField(max_length = 10, choices=platformArray, default ='android')
    is_staff = models.BooleanField(_('staff'), default = False)
    phone = models.CharField(max_length = 15, null = True, blank = True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


#    is_verified = models.BooleanField(default=True)
    
#    is_subscribed = models.BooleanField(default=False)
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)
#    follow= models.ManyToManyField(User,blank=True, related_name="profile_follow")
#    mobile_number = models.CharField(max_length = 15, null = True,blank = True)
#    dob = models.DateField(null = True, blank = True)
#
#    @receiver(post_save, sender=User)
#    def create_user_profile(sender, instance, created, **kwargs):
#        if created:
#            Profile.objects.create(user=instance)
#
#    @receiver(post_save, sender=User)
#    def save_user_profile(sender, instance, **kwargs):
#        instance.profile.save()