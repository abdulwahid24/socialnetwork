# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django_hstore.fields import DictionaryField

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting clients.'),
    )
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'user'

    def __str__(self):
        try:
            fullname = self.profile.data.get('fullName', '')
            return '{0}'.format(fullname)
        except AttributeError:
            return self.email


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data = DictionaryField(null=True)

    class Meta:
        db_table = 'user_profile'

    @property
    def fullname(self):
        try:
            fullname = self.data.get('fullName', '')
            return '{0}'.format(fullname)
        except AttributeError:
            return self.user.email

    def __str__(self):
        try:
            if not self.fullname:
                return self.data
            return self.fullname
        except AttributeError:
            return self.user.email
