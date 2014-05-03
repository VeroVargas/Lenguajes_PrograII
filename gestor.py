import web

render = web.template.render('./templates/')

urls = (
    '/','index',
    '/','horario',
    '/','agregar',
    '/','consulta',
    '/','menu_agregar',
    '/','agregar_platillo',
    '/','restaurantes',
    '/','platillos',
    '/','busqueda',
    '/agregar','agregar',
    '/consulta','consulta',
    '/restaurantes','restaurantes',
    '/platillos','platillos',
    '/busqueda','busqueda',
    '/agregar_platillo','agregar_platillo',
    '/menu_agregar','menu_agregar',
    '/horario','horario',
)

app = web.application(urls,globals())

class index:
    def GET(self):
        return render.index()

class menu_agregar:
        def GET(self):
                return render.menu_agregar()
	def POST(self):
		i = web.input()
        	raise web.seeother('/agregar')

class consulta:
        def GET(self):
                return render.consulta()
	def POST(self):
		i = web.input()
        	raise web.seeother('/consulta')

class restaurantes:
        def GET(self):
                return render.restaurantes()
	def POST(self):
		i = web.input()
        	raise web.seeother('/restaurantes')

class platillos:
        def GET(self):
                return render.platillos()
	def POST(self):
		i = web.input()
        	raise web.seeother('/platillos')

class busqueda:
        def GET(self):
                return render.busqueda()
	def POST(self):
		i = web.input()
        	raise web.seeother('/busqueda')

class agregar_platillo:
        def GET(self):
                return render.agregar_platillo()
	def POST(self):
		i = web.input()
                restaurante=i.txtRestaurante
                platillo=i.txtPlatillo
                tipo=i.tipos
                pais=i.pais
                ingredientes=i.ingredientes
        	raise web.seeother('/agregar_platillo')

class agregar:
        def GET(self):
                return render.agregar()
	def POST(self):
		i = web.input()
        	nombre=i.txtNombre
		comida=i.txtComida
		ubicacion=i.txtUbicacion
		telefono=str(i.txtTelefono)
        	raise web.seeother('/agregar')

class horario:
	def GET(self):
                return render.horario()
        def POST(self):
		i = web.input()
        	raise web.seeother('/agregar')

if __name__ == "__main__":
        app.run()
