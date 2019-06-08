import OpenGL 
#OpenGL.ERROR_ON_COPY = True
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
x0, y0, x1, y1, temp= 0, 0, 0, 0, 0
def initiate(r,g,b):
    glClearColor(r,g,b,0.0)    
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (0.0, 1000.0, 0.0, 1000.0)
def showtheline():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(501,0)   
    glVertex2f(501,1000)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0,501)   
    glVertex2f(1000,501)
    glEnd()
    glColor3f(0.0, 0.0, 0.0)
    x=x0
    y=y0
    dy=y1-y0
    dx=x1-x0
    if(dx==0):
	    d=dy-2*dx
	    dne=2*(dy-dx)
	    de=2*dx
	    while(y!=y1) :
	       if(d<0) :
		   x+=1
		   d+=dne
	       elif(d>0):
		   d+=de   
	       y+=1
	       glBegin(GL_POINTS)
	       glVertex2f(x, y)      
	       glEnd()  
	       glutSwapBuffers()   
	       glFlush()
	       time.sleep(0.01)
    elif(dy/dx>=-1 and dy/dx<=1):
	    d=2*dy-dx
	    dne=2*(dy-dx)
	    de=2*dy
	    while(x!=x1) :
	       if(d>0) :
		   y+=1
		   d+=dne
	       elif(d<0):
		   d+=de   
	       x+=1
	       glBegin(GL_POINTS)
	       glVertex2f(x,y)      
	       glEnd()  
	       glutSwapBuffers()   
	       glFlush()
	       time.sleep(0.01)
    elif(dy/dx>=1):
	    d=dy-2*dx
	    dne=2*(dy-dx)
	    de=2*dx
	    while(y!=y1) :
	       if(d<0) :
		   x+=1
		   d+=dne
	       elif(d>0):
		   d+=de   
	       y+=1
	       glBegin(GL_POINTS)
	       glVertex2f(x, y)      
	       glEnd()  
	       glutSwapBuffers()   
	       glFlush()
	       time.sleep(0.01)
    else:
	    d=dx+2*dy
	    dne=2*(dy+dx)
	    de=-2*dy
	    while(y!=y1) :
	       if(d>0) :
		   x+=1
		   d+=dne
	       elif(d<0):
		   d+=de   
	       y-=1
	       glBegin(GL_POINTS)
	       glVertex2f(x, y)      
	       glEnd()  
	       glutSwapBuffers()   
	       glFlush()
	       time.sleep(0.01)
    glFlush()
x0=int(input())
y0=int(input())
x1=int(input())
y1=int(input())

x0 = 0 + (x0 - 0) * (1000 / float(1500))
y0 = 0 + (y0 - 0) * (1000 / float(1500))
x1 = 0 + (x1 - 0) * (1000 / float(1500))
y1 = 0 + (y1 - 0) * (1000 / float(1500))
print "Viewport Coordinates:",
print x0,y0,x1,y1
x0=int(x0+500);
y0=int(y0+500);
x1=int(x1+500);
y1=int(y1+500);
if(x0>x1):
	temp=x0
	x0=x1
	x1=temp
	temp=y0
	y0=y1
	y1=temp
elif(x0==x1):
	if(y0>y1):
		temp=y0
		y0=y1
		y1=temp
glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(1000, 1000)                      
glutInitWindowPosition(0, 0)                 
window=glutCreateWindow("Scan Conversion")
initiate(0.5,0.7,0.5)
glutDisplayFunc(showtheline)                                               
glutMainLoop()  
