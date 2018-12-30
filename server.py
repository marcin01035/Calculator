import Pyro4

@Pyro4.expose
class calculator():
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



#server runs
disp = calculator()
daemon = Pyro4.Daemon(host="192.168.8.110", port=9999)
daemon = Pyro4.Daemon.serveSimple(
    { disp: "test.Server" },
    ns=False,
    daemon=daemon,
    verbose=True
)

