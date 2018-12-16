import Pyro4

@Pyro4.expose

class calc(object):
	def sum(self, x, y):
		result = x+y
		return result

	def difference(self, x, y):
		result = x - y
		return result

	def product(self, x, y):
		result = x*y
		return result

	def quotient(self, x, y):
		result = x/y
		return result
############################################################################
#powolanie servera
daemon = Pyro4.Daemon()  			#tworzenie Deamona dla Pyro
uri = daemon.register(calc)			#binding MyClass jako obiet Pyro

print("Server ruszyl.  Objekt uri= ", uri)		#wypisanie adresu uri
daemon.requestLoop()				#tryb nasluchiwania deamona

