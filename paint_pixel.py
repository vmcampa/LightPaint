import unicornhat as uh
from time import sleep
import json

class Pixel():
	''' clase para describir pixeles en el UnicornHat '''
	
	def __init__(self):
		''' atributos al inicio '''
		
		self.brillo = 0.25
		self. rotacion = 0
		self.x_pos = 0
		self.y_pos = 0
		self.color = (255, 255, 255)
		self.memory_color = (255,255,255)
		self.canvas = []
		
	def iniciar(self):
		uh.brightness(self.brillo)
		uh.rotation(self.rotacion)
	
	def old_color(self):
		return(uh.get_pixel(self.x_pos, self.y_pos))

	def pintar_pixel(self):
		uh.set_pixel(self.x_pos, self.y_pos, self.color[0], self.color[1], self.color[2])
		uh.show()
		
	def pintar_old_pixel(self):
		uh.set_pixel(self.x_pos, self.y_pos, self.memory_color[0], self.memory_color[1], self.memory_color[2])
		uh.show()
		
	def borrar_canvas(self):
		uh.clear()
		uh.show()
		
	def memorizar_canvas(self):
		self.canvas = uh.get_pixels()
		
	def salvar_canvas(self, filename):
		with open('images/imagen_' + filename + '.json', 'w') as j_obj:
			json.dump(self.canvas, j_obj)
			
	def cargar_canvas(self, filename):
		try:
			with open(filename, 'r') as j_obj:
				loaded_canvas = json.load(j_obj)
				uh.set_pixels(loaded_canvas)
				uh.show()
		except:
			uh.set_pixels(self.canvas)
			uh.show()
			
	def parpadear(self):
		for i in range(3):
			uh.set_all(200,200,200)
			uh.show()
			sleep(0.25)
			uh.clear()
			uh.show()
			sleep(0.5)
			
			
		
	

