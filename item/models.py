# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

#Good

class Good_additional(models.Model):
	name = models.CharField(max_length=1000, verbose_name='Название')
	image = models.ImageField(upload_to='image', verbose_name='Фото', blank=True)
	price = models.IntegerField(verbose_name='Цена',default=0)

	class Meta:
		verbose_name = 'Доп. товар'        
		verbose_name_plural = 'Доп. товары'
	def __unicode__(self):
		return u'%s | %s | %s' % (self.id, self.name, self.price)

class Good(models.Model):
	image = models.ImageField(upload_to='image', verbose_name='Фото', blank=True)
	name = models.CharField(max_length=1000, verbose_name='Название')
	description = models.TextField(max_length=1000, verbose_name='Описание', blank=True)
	price = models.IntegerField(verbose_name='Цена',default=0)
	good_additional = models.ManyToManyField(Good_additional, verbose_name='Комплектация')

	power = models.CharField(max_length=250, verbose_name='Мощность', blank=True)
	voltage = models.CharField(max_length=250, verbose_name='Напряжение', blank=True)
	number_of_phases = models.CharField(max_length=250, verbose_name='Количество фаз', blank=True)
	continuous_operation = models.CharField(max_length=250, verbose_name='Время непрерывной работы', blank=True)
	startup_type = models.CharField(max_length=250, verbose_name='Тип запуска', blank=True)
	power_dvig = models.CharField(max_length=250, verbose_name='Тип двигателя', blank=True)
	displacement = models.CharField(max_length=250, verbose_name='Объем двигателя', blank=True)
	number_of_cylinders = models.CharField(max_length=250, verbose_name='Кол-во цилиндров', blank=True)
	rotational_speed = models.CharField(max_length=250, verbose_name='Частота вращения', blank=True)
	cooling_system = models.CharField(max_length=250, verbose_name='Система охлаждения', blank=True)
	fuel = models.CharField(max_length=250, verbose_name='Вид топлива', blank=True)
	fuel_consumption = models.CharField(max_length=250, verbose_name='Расход топлива', blank=True)
	fuel_capacity = models.CharField(max_length=250, verbose_name='Объем топливного бака', blank=True)
	performance = models.CharField(max_length=250, verbose_name='Исполнение', blank=True)
	dimensions = models.CharField(max_length=250, verbose_name='Размеры (ДхШхВ)', blank=True)
	weight = models.CharField(max_length=250, verbose_name='Вес', blank=True)
	noise_level = models.CharField(max_length=250, verbose_name='Уровень шума', blank=True)
	fabric = models.CharField(max_length=250, verbose_name='Производитель', blank=True)

	def get_additional_good(self):
		return Good_additional.objects.filter(good__id=self.id)

	class Meta:
		verbose_name = 'Товар'        
		verbose_name_plural = 'Товары'
	def __unicode__(self):
		return u'%s | %s | %s' % (self.id, self.name, self.price)
	
	




#Good_additional

#Slide

#Text
