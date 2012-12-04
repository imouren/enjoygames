# -*- coding: utf-8 -*-
import hashlib
from django.db import models
from django.core.cache import cache
from datetime import date, datetime, timedelta

class RechargeLog(models.Model):
    uid = models.CharField(max_length=100)
    type  = models.CharField(max_length=32)
    receipt = models.TextField(max_length=10000)
    ln = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'loowar_rechargelog'
