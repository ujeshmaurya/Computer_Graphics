from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import time

def polygon():
    p = int(input("Enter Number of Points "))
    ta,tb,a,b,sa,sb=0,0,0,0,0,0
    #print "haha"
    for i in range(p):
      a,b = map(int, sys.stdin.readline().split())
      if i:
        glBegin(GL_LINES)
        glVertex2f(ta, tb)
        glVertex2f(a+250, b+250)
        glEnd()
      else:
        sa=a+250
        sb=b+250
      ta=a+250
      tb=b+250
    glBegin(GL_LINES)
    glVertex2f(ta, tb)
    glVertex(sa, sb)
    glEnd()
    



def axes():
	glBegin(GL_LINES)
	glVertex2f(250, 0)
	glVertex2f(250, 500)
	glVertex2f(0, 250)
	glVertex2f(500, 250)
	glEnd()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw():                                            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()                                   
    refresh2d(500, 500)                           
    glColor3f(1.0, 0.0, 0.0)    
    axes()
    glutSwapBuffers()   
    glFlush()
    glColor3f(1.0, 0.0, 1.0)    
    polygon()   
    glutSwapBuffers()   
    glFlush()
    time.sleep(5)
    sys.exit()




glutInit()                                             
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(500, 500)                      
glutInitWindowPosition(0, 0)       
window = glutCreateWindow("Polygon Making")              
glutDisplayFunc(draw)                                  
glutIdleFunc(draw)                                     
glutMainLoop()  

