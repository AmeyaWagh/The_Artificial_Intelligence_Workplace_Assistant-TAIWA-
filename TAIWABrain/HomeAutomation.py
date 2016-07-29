import xmlrpclib
proxy = xmlrpclib.ServerProxy("http://192.168.0.103:8001/")

class homeautomation:
	def __init__(self):
		pass

	def fan_on(self):
		proxy.fan_on()

	def fan_off(self):
		proxy.fan_off()

	def light_on(self):
		proxy.light_on()

	def light_off(self):
		proxy.light_off()
