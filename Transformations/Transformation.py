from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import time

x0, y0, x1, y1 = 0, 0, 0, 0
points = []

def draw_polygon(points):
	la, lb, sa, sb = 0, 0, 0, 0
	for i in range(len(points)):
		a = points[i][0]
		b = points[i][1]
		if i:
			glBegin(GL_LINES)
			glVertex2f(la + 250, lb + 250)
			glVertex2f(a + 250, b + 250)
			glEnd()
		else:
			sa=a
			sb=b
		la=a
		lb=b
	glBegin(GL_LINES)
	glVertex2f(la + 250, lb  +250)
	glVertex(sa + 250, sb + 250)
	glEnd()

def get_polygon():
    global points
    p = int(input("Enter Number of Points "))
    for i in range(p):
      a,b = map(int, sys.stdin.readline().split())
      points.append([a, b, 1])

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

def multiply(mat):
	global points
	newp = []
	for i in range(len(points)):
		newp.append([0, 0, 0])
	for i in range(len(points)):
		for j in range(3):
			newp[i][j] = 0
			for k in range(3):
				newp[i][j] += points[i][k] * mat[k][j]
	for i in range(len(newp)):
		print(newp[i])
	glColor3f(0.0, 0.0, 0.0)    
	draw_polygon(points)
	glColor3f(1.0, 0.0, 1.0)  
	draw_polygon(newp)
	points = newp

def scale():
      global points
      sys.stdout.write("Enter Scaling Factors in X and Y ")
      sx, sy = map(float, sys.stdin.readline().split())
      multiply([[sx,0,0],[0,sy,0],[0,0,1]])
      
def translate():
      global points
      sys.stdout.write("Enter Translation From X and Y ")
      tx, ty = map(float, sys.stdin.readline().split())
      multiply([[1,0,0],[0,1,0],[tx,ty,1]])


def rotate():
      global points
      sys.stdout.write("Enter Rotation Angle ")
      angle = float(raw_input())
      angle *= pi
      angle /= 180
      multiply([[cos(angle),sin(angle),0],[-sin(angle),cos(angle),0],[0,0,1]])



def shear():
      global points
      sys.stdout.write("Enter Shearing Factors in X and Y ")
      sh_x, sh_y = map(float, sys.stdin.readline().split())
      multiply([[1,sh_y,0],[sh_x,1,0],[0,0,1]])
      
      
      
def reflect_x():
      global points
      print("Reflecting in X")
      multiply([[1,0,0],[0,-1,0],[0,0,1]])
      
      
      
def reflect_y():
      global points
      print("Reflecting in Y")
      multiply([[-1,0,0],[0,1,0],[0,0,1]])



      			
	

cnt = 0
def draw():        
    global points, cnt  
    points = []                                  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()                                   
    refresh2d(500, 500)                           
       
    glColor3f(1.0, 0.0, 0.0)    
    draw_axes()  

    glColor3f(1.0, 0.0, 1.0)    
    get_polygon()   
    
    draw_polygon(points)
    
    glutSwapBuffers()   
    glFlush()
    
    cnt += 1
    if (cnt):
		while(1):
			glColor3f(1.0, 0.0, 0.0)    
			draw_axes()
			time.sleep(2)
			glColor3f(1.0, 1.0, 1.0)  
			print("1. Scale")
			print("2. Translate")
			print("3. Rotate")
			#print("4. Shear")
			print("4. Reflect in X")
			print("5. Reflect in Y")
			print("6. Shear")
			inp = int(raw_input("Enter Your Choice "))
			if inp == 1:
				scale()
			elif inp == 2:
				translate()
			elif inp == 3:
				rotate()
			elif inp == 4:
				reflect_x()
			elif inp == 5:
				reflect_y()
			elif inp == 6:
				shear()
			glutSwapBuffers()   
			glFlush()
                       
    glutSwapBuffers()   
    glFlush()




glutInit()                                             
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(500, 500)                      
glutInitWindowPosition(0, 0)       
window = glutCreateWindow("")              
glutDisplayFunc(draw)                                  
glutIdleFunc(draw)                                     
glutMainLoop()  