from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
window_size, quad, n, d= 0, 0, 0, 0

def init2d(r,g,b,window_size):
	glClearColor(r,g,b,0.0)
	glMatrixMode(GL_PROJECTION)
	gluOrtho2D(0, window_size, 0, window_size)
def draw_axes():
    glColor3f(1.0, 1.0, 1.0) 
    glBegin(GL_LINES)
    glVertex2f(quad,0)
    glVertex2f(quad,window_size)
    glVertex2f(0,quad)
    glVertex(window_size,quad)
    glEnd()

def hsr():
	global intense
	glColor3f(0.0, 1.0, 0.0) 
	for i in range(0,100):
		for j in range(0,100):
			if(intense[i][j]==0):
				glColor3f(0.0, 0.0, 1.0)
			elif(intense[i][j]==1):
				glColor3f(0.0, 1.0, 0.0)
			elif(intense[i][j]==2):
				glColor3f(1.0, 0.0, 1.0)
			else:
				continue
			glBegin(GL_POINTS)
			glVertex2d(i+quad, j+quad)
			glEnd()



def draw():
	global n, window_size                
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	init2d(0.0,0.0,0.0,window_size)                    
	glColor3f(1.0, 0.0, 0.0)      
	draw_axes()
	hsr()
	glutSwapBuffers()

window_size = 500
quad = 250
n = int(input())
color = [-1 for i in range(n+1)];
x=[0 for i in range(n+1)];	y=[0 for i in range(n+1)];	z=[0 for i in range(n+1)]
depth_buf = [[100 for i in range(100)] for j in range(100)]
intense = [[100 for i in range(100)] for j in range(100)]
i=0
while(i<n):
	x[i] = int(input())
	y[i] = int(input())
	z[i] = int(input())
	if(i % 2 == 0):
		color[i] = int(input())
	print(x[i], y[i], z[i])
	i=i+1
i=0
while(i < n-1):
	for j in range(x[i] - 1,x[i+1]):
		for k in range(y[i]-1,y[i+1]):
			if(depth_buf[j][k]>=z[i]):
				depth_buf[j][k] = z[i]
				intense[j][k] = color[i]
	i=i+2

glutInit()                                             
glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(window_size, window_size)                      
glutInitWindowPosition(100, 100) 
                         
window = glutCreateWindow("Hidden Surface Removal")              
glutDisplayFunc(draw)                                 
glutIdleFunc(draw)                              
glutMainLoop() 
