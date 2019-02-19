# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class PhoneNumbers(models.Model):
    phone = PhoneNumberField(unique=True, verbose_name="Phone Number *")

    class Meta:
        db_table = 'phone_numbers'

    def __unicode__(self):
        return str(self.phone)


class TaggedPhoneNumbers(models.Model):
    name = models.CharField(max_length=255)
    i_phone = models.OneToOneField(PhoneNumbers, verbose_name="Phone Number *")
    created_at = models.DateTimeField(default=timezone.now)
    valid_upto = models.DateTimeField()
    enable = models.BooleanField(default=True)
    # added_by = models.ForeignKey('user_management.P	rofile', related_name='added_by')
    last_modified_on = models.DateTimeField(null=True, blank=True)
    # last_modified_by = models.ForeignKey('user_ma	nagement.Profile', related_name='last_modified_by',null=True, blank=True)

    class Meta:
        db_table = 'tagged_phone_numbers'


CALL_DIRECTION_CHOICES = (('i', 'INCOMMING'), ('o', 'OUTGOING'))
class CDRRecording(models.Model):
    i_tagged_phone_numbers = models.ForeignKey(TaggedPhoneNumbers)
    call_direction = models.CharField(max_length=1, choices=CALL_DIRECTION_CHOICES)
    calling_number = models.CharField(max_length=20)
    called_number = models.CharField(max_length=20)
    call_time = models.DateTimeField()
    duration = models.DecimalField(max_digits=15, decimal_places=3)
    remote_ip = models.GenericIPAddressField()
    recording = models.FileField()

    class Meta:
        db_table = 'cdr_recording'


class SystemLogs(models.Model):
    action_by = models.CharField(max_length=128)
    action_date = models.DateTimeField(default=timezone.now)
    action_desc = models.CharField(max_length=256)


    class Meta:
        db_table = 'system_logs'
