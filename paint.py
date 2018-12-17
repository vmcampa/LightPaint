# Importar clase "paint_pixel" donde estan los atributos de un pixel
import paint_pixel as pixel
# Importar el modulo "ctr" para control con el joystick
import paint_ctr as ctr
# Importar "sleep" para Debouncing
from time import sleep
# Importar "glob" para leer la carpeta de imagenes
import glob
# Importar "json" para salvar imagenes
import json
# Importar "datetime" para cronometrar el tiempo
import datetime

# Variables
modo = 'DIBUJAR'
reproduccion = 'OFF' # para reproducir las imagenes salvadas automaticamente
show_time = 5  # Tiempo por imagen en el modo presentacion

# Crear objeto-pixel
px = pixel.Pixel()
px.iniciar()

# Iniciar el joystick
ctr.comprobar_joystick()
px.borrar_canvas()
px.pintar_pixel()


while True:
	
	#MODO DIBUJAR
	while modo == 'DIBUJAR':
		# Mirar el joystick
		(color, movimiento) = ctr.mirar_joystick()
		sleep(0.1) # Debounce
		#CAMBIAR MODO Dibujar vs Salvar/Presentacion
		if color == 'SELECT':
			px.memorizar_canvas()
			px.parpadear()
			print(px.canvas)
			modo = 'PRESENTACION'
			break
		print(modo) # Debug
		print(color, movimiento) # Debug
		# MOVER EL PINCEL
		if movimiento != 'CENTRO':
			# Encender el color memorizado
			px.pintar_old_pixel()
			# Actualizar coordenadas
			if movimiento == 'ARRIBA':
				if px.y_pos < 7:
					px.y_pos = px.y_pos + 1
			elif movimiento == 'ABAJO':
				if px.y_pos > 0:
					px.y_pos = px.y_pos - 1
			elif movimiento == 'OESTE':
				if px.x_pos < 7:
					px.x_pos = px.x_pos + 1
			elif movimiento == 'ESTE':
				if px.x_pos > 0:
					px.x_pos = px.x_pos - 1
			# memorizar el color de la nueva coordenada
			px.memory_color = px.old_color()
			# actualizar color del "pincel" a blanco
			px.color = (255,255,255)
			# Colocar el "pincel"
			px.pintar_pixel()
		
		# COLOREAR
		if color != 'NINGUNO':
			if color == 'AZUL':
				px.color = (0,0,255)
			elif color == 'VERDE':
				px.color = (0,255,0)
			elif color == 'AMARILLO':
				px.color = (255,255,0)	
			elif color == 'ROJO':
				px.color = (255,0,0)
			elif color == 'DCHA':
				px.color = (255,255,255)
			elif color == 'IZQ':
				px.color = (0,0,0)
			px.pintar_pixel()
			px.memory_color = px.old_color()
			
		# BORRAR
		if color == 'START':
			px.borrar_canvas()
	
	# Modo presentacion
	while modo == 'PRESENTACION':
		px.cargar_canvas(px.canvas)
		# Mirar el joystick
		(color, movimiento) = ctr.mirar_joystick()
		sleep(0.1) # Debounce
		saved_images = (glob.glob('./images/*.json')) # Cargar archivos json de imagenes
		# CAMBIAR DE MODO 'SELECT'
		if color == 'SELECT':
			px.parpadear()
			px.borrar_canvas()
			print(px.canvas)
			modo = 'DIBUJAR'
			break
		#SALVAR CUADRO 'DCHA o 'IZQ'
		if color == 'DCHA' or color == 'IZQ':
			px.parpadear()
			fecha = datetime.datetime.now()
			filename = fecha.strftime('%B_%Y_%H:%M')
			px.salvar_canvas(filename)
			print('images/imagen_' + filename + '.json')
		# REPRODUCCION AUTOMATICA Play: 'START' Stop: 'START'
		if color == 'START':
			px.parpadear()
			reproduccion = 'ON'
			while reproduccion == 'ON':
				for image in saved_images:
					if reproduccion == 'OFF':
						break
					else:
						t_start = datetime.datetime.now()
						t_elapsed = 0
						px.cargar_canvas(image)
						print('Imagen: ', image)
						while t_elapsed < show_time:	
							# timer
							t_elapsed = datetime.datetime.now() - t_start
							t_elapsed = t_elapsed.total_seconds()
							#print(t_elapsed)
							(color, movimiento) = ctr.mirar_joystick()
							sleep(0.1)
							# Para romper el loop
							if color == 'START':
								reproduccion = 'OFF'
								px.parpadear()
								px.borrar_canvas()
								break
					
			
		
					
		
	
		
	
	
