from django.contrib import admin
from .models import Configuration, Detail

class ConfigurationAdmin(admin.ModelAdmin):
	list_display = ['processor','ram', 'hdd', 'smps', 'graphics', 'soundcard', 'rs232', 'parallel', 'lan', 'hddbay', 'wipicard', 'systemos', 'others']
	prepopulated_fields = {'slug': ('processor','ram', 'hdd', 'smps', 'graphics', 'soundcard', 'rs232', 'parallel', 'lan', 'hddbay', 'wipicard', 'systemos', 'others', )}
admin.site.register(Configuration, ConfigurationAdmin)

class DetailAdmin(admin.ModelAdmin):
	list_display = ['customer', 'chasis', 'configuration', 'assembled_on', 'assembled_by']
	search_fields = ['chasis_serial']
	list_filter = ['customer', 'assembled_on', 'assembled_by']
admin.site.register(Detail, DetailAdmin)
	
	
	
