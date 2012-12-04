# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from apps.helper import *
from apps.cache import *


def index(request):
    type = request.POST.get('type', None) or request.GET.get('type', 'ipad')
    receipt = request.POST.get('receipt',None) or request.GET.get('receipt','')
    uid = request.POST.get('uid',None) or request.GET.get('uid','none')
    ln = request.POST.get('ln', None) or request.GET.get('ln', 'zh-Hans')

    if verify_receipts(receipt):
        res = 1 #
    else:
        res = 0
    if res == 1:
        new_a_log(uid, type, receipt, ln)
    
    data = {'result':res}

    response = HttpResponse(simplejson.dumps(data))
    response['Content-type'] = 'application/json'
    return response
