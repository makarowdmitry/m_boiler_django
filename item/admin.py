from django.contrib import admin
from item.models import * 

# Register your models here.
admin.site.register(Good)
admin.site.register(Good_additional)

# class Good(admin.ModelAdmin):
# 	description = {
# 		models.TextField: {'widget': Textarea(
# 						attrs={'rows': 1,
# 						'cols': 40})},
# 	}
