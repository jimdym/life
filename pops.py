# this file will contain functions that make the initial cell populations
import random
from cell import Cell


def read_from_file(alist, a, pen,cell_size):
	# prompt the user for a file and save alist there
	fname=input('Enter the name of the file to read from: ')
	print('readingfrom '+ fname)
	# need to prompt for comments before finishing
	f=open(fname,'r')
	for line in f:
		s=line.split(',')
		x=int(s[0])
		y=int(s[1])
		t=str(x)+','+str(y)
		a[t]='lit'
		alist.append(Cell(x,y,"square","yellow",'lit',cell_size))
	f.close()
	for cell in alist:
		print (cell)
	#p=input('still in read from file')
# end definition of function to populate alist from a file

def pop1(alist,a, pen):
	# just 3 cells in a row
	alist.append(Cell(0,0,"square","yellow",'lit',cell_size))
	a['0,0']='lit'
	alist[0].render(pen)
	alist.append(Cell(0,1,"square","white",'lit',cell_size))
	a['0,1']='lit'
	alist[1].render(pen)
	alist.append(Cell(0,2,"square","blue",'lit',cell_size))
	a['0,2']='lit'
	alist[2].render(pen)
	for cell in alist:
		print(cell)
# end function to define vertical bar list



def pop2(alist, a, pen,cell_size):
	# ask user for number of initial cells and size of grid to populate
	# randomly places cells
	while True:
		try:
			r=int(input('Enter the number of cells to populate '))
		except:
			print('No. it has to be an integer. Try again.')
			continue
		else:
			print('OK. There will be ' + str(r) + ' cells lit initially')
			break
	print('The grid size where the initial population goes needs to be pretty small')
	print('	else it will most likely die out quickly. Try something like 3.')
	while True:
		try:
			g=int(input('Size of the initial grod of cells '))
		except:
			print('No. it has to be an integer. Try again.')
			continue
		else:
			print('OK. Initial population of ' + str(r) + ' will go into a ' + str(g) + ' grid')
			break
	for i in range(r):
		x = random.randint(-g, g)
		y = random.randint(-g, g)
		s=str(x)+','+str(y)
		if s in a:
			# s needs to be unique, but I can see creating an infinite loop here
			while s in a:
				x = random.randint(-g, g)
				y = random.randint(-g, g)
				s=str(x)+','+str(y)
		alist.append(Cell(x,y,"square","yellow",'lit',cell_size))
		a[s]='lit'
		alist[i].render(pen)
	print('Initial cell population')
	for cell in alist:
		print(cell)
# end definition of pop2 function
