from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import time

x0, y0, x1, y1 = 0, 0, 0, 0
pts = []
last = []
hflag = 0
def draw_cube(pts):
	for x in range(6):
		glColor3f(1.0, 0.0, 0.0)  
		glBegin(GL_QUADS)
		for i in range(4):
			a = pts[x * 4 + i][0]
			b = pts[x * 4 + i][1]
			glVertex2f(a + 250, b + 250)
		glEnd()
	for x in range(6):
		glColor3f(0.0, 1.0, 0.0)  
		glBegin(GL_LINES)
		for i in range(4):
			if i:
				glVertex2f(pts[x * 4 + i][0] + 250, pts[x * 4 + i][1] + 250)
				glVertex2f(pts[x * 4 + i - 1][0] + 250, pts[x * 4 + i - 1][1] + 250)
			else:
				glVertex2f(pts[x * 4 + i][0] + 250, pts[x * 4 + i][1] + 250)
				glVertex2f(pts[x * 4 + i + 3][0] + 250, pts[x * 4 + i + 3][1] + 250)
		glEnd()
		

def draw_last_cube(pts):
	for x in range(6):
		glColor3f(0.0, 0.0, 0.0)  
		glBegin(GL_QUADS)
		for i in range(4):
			a = pts[x * 4 + i][0]
			b = pts[x * 4 + i][1]
			glVertex2f(a + 250, b + 250)
		glEnd()
	for x in range(6):
		glColor3f(0.0, 0.0, 0.0)  
		glBegin(GL_LINES)
		for i in range(4):
			if i:
				glVertex2f(pts[x * 4 + i][0] + 250, pts[x * 4 + i][1] + 250)
				glVertex2f(pts[x * 4 + i - 1][0] + 250, pts[x * 4 + i - 1][1] + 250)
			else:
				glVertex2f(pts[x * 4 + i][0] + 250, pts[x * 4 + i][1] + 250)
				glVertex2f(pts[x * 4 + i + 3][0] + 250, pts[x * 4 + i + 3][1] + 250)
		glEnd()



def get_cube():
    global pts, last
    for i in range(24):
      a,b,c = map(int, sys.stdin.readline().split())
      pts.append([a, b, c, 1])
    last = pts

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
	global pts, last
	newp = []
	for i in range(len(pts)):
		newp.append([0, 0, 0, 0])
	for i in range(len(pts)):
		for j in range(4):
			newp[i][j] = 0
			for k in range(4):
				newp[i][j] += pts[i][k] * mat[k][j]
	for i in range(len(pts)):
		for j in range(4):
			newp[i][j] /= newp[i][3]
	for i in range(len(newp)):
		print(newp[i])
	draw_cube(newp)
	last = newp

def parallel_gen():
	sys.stdout.write("Enter Direction Vector of parallel rays: ")
	a,b,c = map(int, sys.stdin.readline().split())
	sys.stdout.write("Enter Direction Cosines of Normal to Plane of Projection ")
	n1,n2,n3 = map(int, sys.stdin.readline().split())
	sys.stdout.write("Enter Reference Point in Plane of Projection ")
	x0,y0,z0 = map(int, sys.stdin.readline().split())
	d0 = x0 * n1 + y0 * n2 + z0 * n3
	d1 = a * n1 + b * n2 + c * n3
	d = d0 - d1
	multiply([[-1*a * n1 + d1,-1*b * n1,-1*c * n1,0],[-1*a * n2,-1*b * n2 + d1,-1*c * n2,0],[-1*a * n3,-1*b * n3,-1*c * n3 + d1,0],[a*d0,b*d0,c*d0,d1]])

      
def parallel_cav():
	alpha = 45
	sys.stdout.write("Enter Angle of Projected Line with X-Axis ")
	phi = float(sys.stdin.readline())
	phi = pi / 180 * phi 
	if alpha == 90:
		L = 0
	else:
		alpha = pi / 180 * alpha
		L = 1 / tan(alpha)
	multiply([[1,0,0,0],[0,1,0,0],[L * cos(phi),L * sin(phi),0,0],[0,0,0,1]])
	
def parallel_cab():
	alpha = 63.4
	sys.stdout.write("Enter Angle of Projected Line with X-Axis ")
	phi = float(sys.stdin.readline())
	phi = pi / 180 * phi 
	if alpha == 90:
		L = 0
	else:
		alpha = pi / 180 * alpha
		L = 1 / tan(alpha)
	multiply([[1,0,0,0],[0,1,0,0],[L * cos(phi),L * sin(phi),0,0],[0,0,0,1]])
	
def parallel_ortho():
	alpha = 90
	phi = 90
	phi = pi / 180 * phi 
	if alpha == 90:
		L = 0
	else:
		alpha = pi / 180 * alpha
		L = 1 / tan(alpha)
	multiply([[1,0,0,0],[0,1,0,0],[L * cos(phi),L * sin(phi),0,0],[0,0,0,1]])
	
def perspective():
      sys.stdout.write("Enter Coordinates of Center of Projection ")
      a,b,c = map(int, sys.stdin.readline().split())
      sys.stdout.write("Enter Direction Cosines of Normal to Plane of Projection ")
      n1,n2,n3 = map(int, sys.stdin.readline().split())
      sys.stdout.write("Enter Reference Point in Plane of Projection ")
      x0,y0,z0 = map(int, sys.stdin.readline().split())
      d0 = x0 * n1 + y0 * n2 + z0 * n3
      d1 = a * n1 + b * n2 + c * n3
      d = d0 - d1
      multiply([[a * n1 + d,b * n1,c * n1,n1],[a * n2,b * n2 + d,c * n2,n2],[a * n3,b * n3,c * n3 + d,n3],[-a * d1 - a * d,-b * d1 - b * d,-c * d1 - c * d,-d1]])


      			
	

cnt = 0
def draw():        
    global pts, cnt, last
    pts = []                                  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()                                   
    refresh2d(500, 500)                           
       
    glColor3f(0.0, 1.0, 0.0)    
    draw_axes()  

    glColor3f(1.0, 0.0, 0.0)    
    get_cube()   
    
    draw_cube(pts)
    
    glutSwapBuffers()   
    glFlush()
    cnt += 1
    if (cnt):
		while(1):
			draw_last_cube(last)
			glColor3f(0.0, 1.0, 0.0)    
			draw_axes()
			glColor3f(1.0, 1.0, 1.0)  
			print("1. Enter 1 for Parallel(Orthographic)")
			print("2. Enter 2 for Cabinet")
			print("3. Enter 3 for Cavalier")
			print("4. Enter 4 for General Parallel")
			print("5. Enter 5 for Perspective")
			inp = int(raw_input("Enter Your Choice "))
			if inp == 1:
				parallel_ortho()
			if inp == 2:
				parallel_cab()
			if inp == 3:
				parallel_cav()
			if inp == 4:
				parallel_gen()
			if inp == 5:
				perspective()
			glutSwapBuffers()   
			glFlush()
			time.sleep(2)
                       
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


