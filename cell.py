class Cell():
	# this gets put on the screen
	def __init__(self, x, y, shape, color,status, cell_size):
		self.x=x
		self.y=y
		self.shape=shape
		self.color=color
		self.status=status
		self.cell_size=cell_size
		self.neighbors=0
		
	def render(self, pen):
		pen.goto(self.x*self.cell_size,self.y*self.cell_size)
		pen.shape(self.shape)
		pen.shapesize(self.cell_size/20, self.cell_size/20)
		pen.color(self.color)
		pen.stamp()
	
	def neigh_count(self, a, ulist):
		# count the adjacent cells that are lit (self.neighbors)
		# update a list of unlit cells (ulist))
		self.neighbors=0
		x1=self.x
		y1=self.y+1
		one=str(x1)+','+str(y1)
		if one in a:
			self.neighbors+=1
		else:
			ulist.append(Cell(x1,y1,'square','yellow','unlit',self.cell_size))
		x2=self.x+1
		y2=self.y+1
		two=str(x2)+','+str(y2)
		if two in a:
			self.neighbors+=1
		else:
			ulist.append(Cell(x2,y2,'square','yellow','unlit',self.cell_size))
		x3=self.x+1
		y3=self.y
		three=str(x3)+','+str(y3)
		if three in a:
			self.neighbors+=1
		else:
			ulist.append(Cell(x3,y3,'square','yellow','unlit',self.cell_size))
		x4=self.x+1
		y4=self.y-1
		four=str(x4)+','+str(y4)
		if four in a:
			self.neighbors+=1
		else:
			ulist.append(Cell(x4,y4,'square','yellow','unlit',self.cell_size))
		x5=self.x
		y5=self.y-1
		five=str(x5)+','+str(y5)
		if five in a:
			self.neighbors+=1
		else:
			ulist.append(Cell(x5,y5,'square','yellow','unlit',self.cell_size))
		x6=self.x-1
		y6=self.y-1
		six=str(x6)+','+str(y6)
		if six in a:
			self.neighbors+=1
		else:
			ulist.append(Cell(x6,y6,'square','yellow','unlit',self.cell_size))
		x7=self.x-1
		y7=self.y
		seven=str(x7)+','+str(y7)
		if seven in a:
			self.neighbors+=1
		else:
			ulist.append(Cell(x7,y7,'square','yellow','unlit',self.cell_size))
		x8=self.x-1
		y8=self.y+1
		eight=str(x8)+','+str(y8)
		if eight in a:
			self.neighbors+=1
		else:
			ulist.append(Cell(x8,y8,'square','yellow','unlit',self.cell_size))
	# end neigh_count method definition
		
	def __str__(self):
		s=str(self.x)+','+str(self.y)+','+str(self.neighbors)+','+str(self.status)
		return s
# end class cell definition
