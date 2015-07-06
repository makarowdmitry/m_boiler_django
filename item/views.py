# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from item.models import *
from django.core.urlresolvers import reverse
from operator import itemgetter
import datetime
from django.db.models import Count, Min, Sum
from django.db import connection
from django.core.mail import send_mail

# Create your views here.
def index(request):
	goods = Good.objects.all()
	return render_to_response('index.html',{'goods':goods})

def filter_goods(request):
	if request.method == 'POST':
		price_left = request.POST.get('price_left', '')
		price_right = request.POST.get('price_right', '')
		power_left = request.POST.get('power_left', '')
		power_right = request.POST.get('power_right', '')
		fabric = request.POST.get('fabric', '')
		fuel = request.POST.get('fuel', '')
		

	return HttpResponse('ok')


