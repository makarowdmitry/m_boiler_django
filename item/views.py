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
import json

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

		price_interval = [x for x in range(int(price_left),int(price_right)+1)]
		power_interval = [x for x in range(int(power_left),int(power_right)+1)]

		# all_entries = Good.objects.filter(price__in=price_interval).filter(power__in=power_interval)
		if fabric == 'none' and fuel  == 'none':
			all_entries_full = Good.objects.filter(price__in=price_interval).filter(power__in=power_interval)
		elif fuel  == 'none':
			all_entries_full = Good.objects.filter(price__in=price_interval).filter(power__in=power_interval).filter(fabric__iexact=fabric)
		elif fabric == 'none':
			all_entries_full = Good.objects.filter(price__in=price_interval).filter(power__in=power_interval).filter(fuel__iexact=fuel)
		else:
			all_entries_full = Good.objects.filter(price__in=price_interval).filter(power__in=power_interval).filter(fuel__iexact=fuel).filter(fabric__iexact=fabric)

		
		data2 = []
		for item in all_entries_full.values():
			additional_goods = list(Good_additional.objects.filter(good__id=item['id']).values())
			# item['additional_goods'] = list(item.get_additional_good)
			item.update({'additional_goods': additional_goods})
			new_list = data2.append(item)


		# data_send = { key:value for item in all_entries_full.values()}
		# data = json.dumps(data_send)
		# data = [{'one': '1', 'two': '3'},{'one': '2', 'two': '4'}]

		
		# all_entries = Good.objects.filter(price__in=price_interval).filter(power__in=power_interval).filter(fuel__iexact=fuel).filter(fabric__iexact=fabric)

	# Выбрать товары с данными параметрами и отсортировать по цене. Дешевые сначала.
	# Упаковать в json. отправить на сервер
	return HttpResponse(json.dumps(data2), content_type='application/json')

	# return HttpResponse(json.dumps(all_entries_full.values_list()), content_type="application/json")

def email_form(request):
	if request.method == 'POST':
		name = request.POST.get('name', '')
		phone = request.POST.get('phone', '')
		subject = u'Заявка  - {0}, {1}'.format(name,phone)
		message1 = u'Имя: {0}<br/>Телефон: {1}<br/>'.format(name,phone)
		message = u'{0} {1}'.format(name,phone)

		send_mail(subject, message, 'ppetroenergo@mail.ru', ['makarow.dmitry@gmail.com'], fail_silently=False, html_message=message1)
	
	return HttpResponse([phone,name])