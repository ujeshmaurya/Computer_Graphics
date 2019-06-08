from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import time

x0, y0, x1, y1 = 0, 0, 0, 0
points = []
viewer = [-10, -10, 1000]

def cross_product(v1, v2):
	return [v1[1] * v2[2] - v2[1] * v1[2], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v2[0] * v1[1]]
	
def dot_product(v1, v2):
	return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

def isVisible(x, points):
	v1 = [points[x * 4 + 0][0] - points[x * 4 + 1][0], points[x * 4 + 0][1] - points[x * 4 + 1][1], points[x * 4 + 0][2] - points[x * 4 + 1][2]]
	v2 = [points[x * 4 + 0][0] - points[x * 4 + 2][0], points[x * 4 + 0][1] - points[x * 4 + 2][1], points[x * 4 + 0][2] - points[x * 4 + 2][2]]
	n = cross_product(v1, v2)
	c = []
	if (x):
		c = [points[x * 4 - 3][0] - points[x * 4 + 0][0], points[x * 4 - 3][1] - points[x * 4 + 0][1], points[x * 4 - 3][2] - points[x * 4 + 0][2]]
	else:
		c = [points[x * 4 + 7][0] - points[x * 4 + 0][0], points[x * 4 + 7][1] - points[x * 4 + 0][1], points[x * 4 + 7][2] - points[x * 4 + 0][2]]
	if (dot_product(n, c) > 0):
		n[0] = -n[0]
		n[1] = -n[1]
		n[2] = -n[2]
	view = [viewer[0] - points[x * 4 + 0][0], viewer[1] - points[x * 4 + 0][1], viewer[2] - points[x * 4 + 0][2]]
	print(n, c)
	if (dot_product(view, n) > 0): return True
	else: return False

def draw_cube(points):
	for x in range(6):
		glColor3f(1.0, 0.0, 1.0)
		if not isVisible(x, points): continue
		print(x)
		glBegin(GL_QUADS)
		for i in range(4):
			a = points[x * 4 + i][0]
			b = points[x * 4 + i][1]
			glVertex2f(a + 250, b + 250)
		glEnd()
		glColor3f(0.0, 1.0, 0.0)
		glBegin(GL_LINES)
		for i in range(4):
			if i:
				glVertex2f(points[x * 4 + i][0] + 250, points[x * 4 + i][1] + 250)
				glVertex2f(points[x * 4 + i - 1][0] + 250, points[x * 4 + i - 1][1] + 250)
			else:
				glVertex2f(points[x * 4 + i][0] + 250, points[x * 4 + i][1] + 250)
				glVertex2f(points[x * 4 + i + 3][0] + 250, points[x * 4 + i + 3][1] + 250)
		glEnd()
		

def get_cube():
    global points, last
    for i in range(24):
      a,b,c = map(int, sys.stdin.readline().split())
      points.append([a, b, c, 1])
    last = points

def draw_point(x, y):
  glBegin(GL_POINTS)
  glVertex2f(x,y)
  glEnd()
  #glutSwapBuffers()   
  #glFlush()         


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_axes():
	glBegin(GL_LINES)
	glVertex2f(250, 0)
	glVertex2f(250, 500)
	glVertex2f(0, 250)
	glVertex2f(500, 250)
	glEnd()



def draw():        
    global points, cnt, last
    points = []                                  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()                                   
    refresh2d(500, 500)                           
       
    glColor3f(1.0, 0.0, 0.0)    
    draw_axes()  

    glColor3f(1.0, 0.0, 1.0)    
    get_cube()   
    
    draw_cube(points)
                       
    glutSwapBuffers()   
    glFlush()
    
    while(1):
    	continue




glutInit()                                             
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(500, 500)                      
glutInitWindowPosition(0, 0)       
window = glutCreateWindow("")              
glutDisplayFunc(draw)                                  
glutIdleFunc(draw)                                     
glutMainLoop()  


