''' Control del robot con el joystick '''

import sys
import pygame

# Diccionario para asignar cada boton a su color
BOTONES = {0:'AZUL', 1:'ROJO', 2:'AMARILLO', 3:'VERDE', 4:'IZQ', 5:'DCHA', 8:'SELECT', 9:'START', 10:'NINGUNO'}
boton = BOTONES[10]
# Diccionario para asignar los ejes
EJES = {(1,-1):'ARRIBA', (1,1):'ABAJO', (0,1):'ESTE', (0,-1):'OESTE', (1,0):'CENTRO', (0,0):'CENTRO'}
eje = EJES[(0,0)]

def comprobar_joystick():
		# Comprobar si hay un joystick conectado e inicializarlo
		pygame.init()
		joystick_count = pygame.joystick.get_count()
		print('\nHay ' + str(joystick_count) + ' joystick/s conectado')

		if joystick_count == 0:
			print('no ha joystick')
			pygame.quit()
			sys.exit()
		else:
			joystick = pygame.joystick.Joystick(0)
			joystick.init()
			ejes = joystick.get_numaxes()
			botones = joystick.get_numbuttons()
			hats = joystick.get_numhats()
			print('Hay :' + str(ejes) + ' ejes')
			print('Hay :' + str(botones) + ' botones')
			print('Hay :' + str(hats) + ' hats')
			
def mirar_joystick(): # crear en otro archivo un objeto "robot" para modificar sus atributos
		#BOTONES
		# Comprobar si alguno de los , botones de los ejes ha sido presionado
		global boton, eje
		for event in pygame.event.get(): # idenficar el boton presionado
			if event.type == pygame.JOYBUTTONDOWN: 
				boton = BOTONES[event.button]
				print('Boton Apretado: ' + boton)
				
			elif event.type == pygame.JOYBUTTONUP: # identificar liberacion
				boton = BOTONES[10] # solo hay nueve botones
				print('Boton Soltado: ' + boton)
			
	# EJES
	# Comprobar si alguno de los botones de los ejes ha sido presionado
			if event.type == pygame.JOYAXISMOTION: # and event.value < -0.2) or (event.type == pygame.JOYAXISMOTION and event.value > 0.2):
				eje = EJES[(int(event.axis), int(event.value))]
				print('Eje apretado: ', eje)
		return(boton, eje)


	
