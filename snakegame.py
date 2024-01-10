from sys import platform
from pytimedinput import timedInput
import os
from colorama import Fore, init

import random
import time

init(autoreset=True)
def print_field():
	for cell in CELLS:
		if cell in snake_body: 
			print(Fore.GREEN + 'S', end='')# check that a tuple is inside a list
		#if cell[0]==0 or cell[1]==(field_height-1) or cell[0]==field_width-1 or cell[1]== 0:
			#print('#')
		elif cell[1] in (0, field_height-1) or cell[0] in (0, field_width-1) : #checks that a number is inside/between two numbers
			if cell[0]==field_width-1:
					print(Fore.CYAN +'#')			
			else: print(Fore.CYAN + '#', end = '')
		elif cell == apple_pos:
			print(Fore.RED +'a', end='')

		else: print(' ', end='')
	
def update_snake():
	global eaten
	#head, middle, tail=snake_body
	#snake_body[0] = (head[0]+direction[0], head[1]+ direction[1])
	#snake_body[1]=head
	#snake_body[2]=middle
	new_head =snake_body[0][0]+direction[0], snake_body[0][1]+ direction[1]
	snake_body.insert(0, new_head)
	if not eaten:
		snake_body.pop()#hard to understand
	eaten=False
	

def apple_collision():
	global apple_pos, eaten
	if apple_pos==snake_body[0]	:
		apple_pos=place_apple()
		eaten=True
		

def place_apple():
	col = random.randint(1, field_width-2)
	row=random.randint(1, field_height-2)
	while (col, row) in snake_body:
		col = random.randint(1,field_width-2)
		row=random.randint(1, field_height-2)
			
	return(col, row)
	


	
	
		
	
#settings
field_width=32#should be uppercase
field_height=16#should be uppercase
CELLS=[(col , row) for row in range(field_height) for col in range(field_width)]
#cells=[]
#for row in range( field_height):
	#for col in range(field_width):
		#cells.append((col,row))
		
if platform == "win32" or platform == "cygwin":
	clearcmd = "cls"
else:
	clearcmd = "clear"

		


#snake
snake_body=[(5,field_height//2), (4,field_height//2),(3, field_height//2)]
DIRECTIONS = {'left':(-1,0), 'right':(1,0), 'up': (0, -1), 'down':(0,1)}
direction =DIRECTIONS['right']

#apple 
apple_pos = place_apple()
eaten=False
os.system(clearcmd)
while True:
	
	# write on top of the field (powershell or terminal)
	print('\033[H')
	
	
	#field drawing
	print_field()

	# get input
	txt,_= timedInput(' ',timeout= 0.3)
	match txt:
		case'w':direction =DIRECTIONS['up']
		case'a':direction =DIRECTIONS['left']
		case's':direction =DIRECTIONS['down']
		case'd':direction =DIRECTIONS['right']
		case'q':
			os.system(clearcmd)
			break


	#commands=input()
	#if txt=='w':
		#direction =DIRECTIONS['up']
	#elif txt=='s':
		#direction =DIRECTIONS['down']
	#elif txt=='d':
		#direction =DIRECTIONS['right']
	#elif txt=='a':
		#direction =DIRECTIONS['left']
	
	#update the game
	update_snake()
	apple_collision()
	if snake_body[0][0] in(0, field_width-1) or snake_body[0][1] in (0, field_height-1) or snake_body[0] in snake_body[1:]:
		print('Sadly, you lost')
		time.sleep(2)
		os.system(clearcmd)
		break
	


	
 
