import xmlrpclib
proxy = xmlrpclib.ServerProxy("http://192.168.0.108:8001/")

class doorlock:
	def __init__(self):
		pass

	def lock(self):
		proxy.lock()

	def unlock(self):
		proxy.unlock()
