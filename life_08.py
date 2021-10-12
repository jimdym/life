# 
# with the 06 version. the basic display and game logic work. File save
# and replay work. Single and multistep modes work. 
#
#	Now on to version 08
#
#	1. sort of trivial but i want to add comments to the saved file
#	done: 2. a way to scale the size of the visible cells. I have it where you
#		can enter size in px
#	done 3. variably increase the size of the screen
#	4. multistep without displaying the steps in order to improve performance
#	5..when selecting stop, also close the graphics screen.

import turtle
import random

from cell import Cell
from pops import pop2
from pops import read_from_file
from setup import sets



def save_to_file(alist):
	# prompt the user for a file and save alist there
	fname=input('Enter the name of the file to write alist to: ')
	print('writing alist to '+ fname)
	# need to prompt for comments before finishing
	f=open(fname,'w')
	for cell in alist:
		s=str(cell.x)+','+str(cell.y)+',\n'
		f.write(s)
	f.close()
# end definition of functino to save alist to a file

# variables named in all caps are going to be global
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CELL_SIZE=20
CELL_COLOR='yellow'
# cells outside the grid will be extinguished
MAX_GRID = 800

# max iterations of the game (to keep from being an infinite loop)
ITER=1500

l=sets(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, CELL_COLOR, MAX_GRID)

SCREEN_WIDTH=l[0]
SCREEN_HEIGHT = l[1]
CELL_SIZE=l[2]
CELL_COLOR=l[3]
MAX_GRID = l[4]

wn = turtle.Screen()
wn.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
wn.title("The game of Life")
wn.bgcolor("black")
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.hideturtle()
pen.penup()

# a is a dictionary to make it easier to find neighbors
a={}
alist=[]
#populates a few cells in a vertical row.
print('How do you want to populate the initial group of cells?')
print('	1 to enter a random population: ')
print('	2 to get a saved group from a file: ')
instr=input('What do you want to do? ')
if instr=='1':
	pop2(alist,a,pen,CELL_SIZE)
elif instr=='2':
	read_from_file(alist, a, pen,CELL_SIZE)
else:
	pop2(alist, a, pen)
# save to initial cell config in case the user wants to save it or replay it
init_list=[]
for cell in alist:
	init_list.append(cell)

pen.clear()
for cell in alist:
	cell.render(pen)
#	wn.update()
# instr=input('Initial screen displays, press enter to go through the main loop')
c=0
# how many steps in a multistep loop
mstep=0
while c<ITER:
	c+=1
	if mstep==0:
		print('Enter a function: ')
		print('	s to stop the program')
		print('	m for multistep')
		print('	f to save the initial config to a file')
		print('	just hit enter to go through the loop again')
		instr=input('Enter a selection here: ')
		if instr == 's':
			break
		if instr == 'm':
			while True:
				try:
					mstep=int(input('Enter the number of steps to take '))
				except:
					print('No. it has to be an integer. Try again.')
					continue
				else:
					print('OK. we do ' + str(mstep) + ' steps')
				break
		if instr == 'f':
			save_to_file(init_list)
			# break
	else:
		mstep-=1
	# calculation next generation
	ulist=[]
	print('iteration '+ str(c))
	for cell in alist:
		#print(cell)
		cell.neigh_count(a,ulist)
		if cell.neighbors <2:
			cell.status='unlit'
		elif cell.neighbors > 3:
			cell.status='unlit'
		elif abs(cell.x) > MAX_GRID or abs(cell.y) > MAX_GRID:
			cell.status='unlit'
			
	t={}
	for cell in ulist:
		s=str(cell.x)+','+str(cell.y)
		if s in t:
			t[s]+=1
		else:
			t[s]=1
	#now get the cells out of t if the count = 3
	# t{} is processed to update alist adding new lit cells
	for i in t:
		if t[i] == 3:
			s=i.split(',')
			x=int(s[0])
			y=int(s[1])
			alist.append(Cell(x,y,'square','yellow','lit',CELL_SIZE))
	tlist=[]
	# lit cells are copied into tlist
	for cell in alist:
		if cell.status=='lit':
			tlist.append(cell)
	alist = tlist
	a={}
	for cell in alist:
		s=str(cell.x)+','+str(cell.y)
		a[s]='lit'
		cell.neighbors=0
	#display the cells
	pen.clear()
	for cell in alist:
		cell.render(pen)
		wn.update()

wn.mainloop()
# end main while loop
# print a summary?
