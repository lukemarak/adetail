from django.db import models

class Configuration(models.Model):
	
	processor = models.CharField(max_length=20, help_text="e.g.i3-3220@3.2", blank=True)
	
	ram = models.CharField(max_length=50, help_text="e.g.4GBDDR3x1", blank=True)
	
	hdd = models.CharField(max_length=100, help_text="e.g. 1TBx1, 1TBx2", blank=True)
	
	smps = models.CharField(max_length=50, help_text="e.g.FSP400W", blank=True)
	
	graphics = models.CharField(max_length=50, help_text="e.g.2GBDDR3Graphic", blank=True)
	
	soundcard = models.CharField(max_length= 50, help_text="1xSoundCard", blank=True)
	
	rs232 = models.CharField(max_length=10, help_text="e.g.2xRS232", blank=True)
	
	parallel = models.CharField(max_length=10, help_text="1xPP", blank=True)
	
	lan = models.CharField(max_length=50, help_text="e.g.1xDualPort", blank=True)
	
	hddbay = models.CharField(max_length=50, help_text="1xRemovalHddBay", blank=True)
	
	wipicard = models.CharField(max_length=20, help_text="1xWipiCard", blank=True)
	
	systemos = models.CharField(max_length=50, help_text="Win-7pro.x32_64", blank=True)
	
	others = models.CharField(max_length=100, help_text="extra", blank=True)
	
	slug = models.SlugField(max_length=200, unique=True)
	
	def __str__(self):
			return self.slug
	
	class Meta:
		ordering = ['processor','ram', 'hdd', 'smps', 'graphics', 'soundcard', 'rs232', 'parallel', 'lan', 'hddbay', 'wipicard', 'systemos', 'others']
		verbose_name = 'configuration'
		verbose_name_plural = 'configurations'
		
		def __str__(self):
			return self.slug
	
	
class Detail(models.Model):
	configuration = models.ForeignKey(Configuration, related_name ='detail', on_delete='models.cascade')
	
	customer = models.CharField(max_length=50, blank=False)
	CHASIS_MODEL = (
		('510', 'IPC-510'),
		('610', 'IPC-610'),
		('A4000', 'ACP-4000'),
		('A4320', 'ACP-4320'),
		('A2010', 'ACP-2010'),
		('A4340', 'ACP-4340'),
		('A4360', 'ACP-4360'),
		
	)
	chasis = models.CharField(max_length=50, choices=CHASIS_MODEL)
	
	chasis_serial = models.CharField(max_length=50)
	
	MOTHERBOARDS = (
		('I701', 'AIMB-701'),
		('I767', 'AIMB-767'),
		('I769', 'AIMB-769'),
		('I780', 'AIMB-780'),
		('I781', 'AIMB-781'),
		('I782', 'AIMB-782'),
		('I785', 'AIMB-785'),
		('I784', 'AIMB-784'),
		('S584', 'ASMB-584'),
		('S784', 'ASMB-784'),
		('S785', 'ASMB-785'),
		('S781', 'ASMB-781'),
		('S782', 'ASMB-782'),
	)
	
	motherboard = models.CharField(max_length=50, choices=MOTHERBOARDS)
	
	board_serial = models.CharField(max_length=50)
	
	smps = models.CharField(max_length=50, blank=True)
	
	ram = models.CharField(max_length=20, blank=True)
	
	hdd = models.CharField(max_length= 20, blank=True)
	
	productkey = models.CharField(max_length=100, blank=True)
	
	others = models.TextField(blank=True)
	
	assembled_by = models.CharField(max_length=50, blank=True)
	
	assembled_on= models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ('assembled_on',)
		
	def __str__(self):
		return self.customer
	
	