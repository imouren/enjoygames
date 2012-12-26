# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from apps.helper import *
from apps.cache import *

OPEN = 1
CLOSE = 0
STATUS = OPEN


def index(request):
    type = request.POST.get('type', None) or request.GET.get('type', 'ipad')
    receipt = request.POST.get('receipt',None) or request.GET.get('receipt','')
    uid = request.POST.get('uid',None) or request.GET.get('uid','none')
    ln = request.POST.get('ln', None) or request.GET.get('ln', 'zh-Hans')
    test = request.POST.get('test', None) or request.GET.get('test', '0')
    
    if test == '1':
        is_test = True
    else:
        is_test = False

    if have_used(uid, receipt):
        res = -1 # receipt has used
    elif verify_receipts(receipt, is_test):
        res = 1 # OK
    else:
        res = 0 # receipt wrong
    if res == 1:
        new_a_log(uid, type, receipt, ln)
    
    data = {'result':res}

    response = HttpResponse(simplejson.dumps(data))
    response['Content-type'] = 'application/json'
    return response

def status(request):
    data = {'result':STATUS}

    response = HttpResponse(simplejson.dumps(data))
    response['Content-type'] = 'application/json'
    return response