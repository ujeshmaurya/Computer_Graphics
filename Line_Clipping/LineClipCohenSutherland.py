from __future__ import division
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             
width, height = 400,400                     
condition=False
completed=False

a1,a2=map(int,raw_input("Enter (x,y) first point : ").split())
b1,b2=map(int,raw_input("Enter (x,y) second point : ").split())
xmin,ymin,xmax,ymax=map(int,raw_input("Enter xmin , ymin , xmax , ymax for clip window : ").split())


def get_outcode(x,y):
    outcode=0x0
    if(y>ymax):
        outcode=outcode+0x8
    elif(y<ymin):
        outcode=outcode+0x4
    if(x>xmax):
        outcode=outcode+0x2
    elif(x<xmin):
        outcode=outcode+0x1
    return outcode


def clip(x0,y0,x1,y1):
    outcode0=get_outcode(x0,y0)
    outcode1=get_outcode(x1,y1)
    global condition,completed
    while(completed==False):
        if(not(outcode0 | outcode1)):
            condition=True
            completed=True
        elif(outcode0 & outcode1):
            completed=True
        else:
            if(outcode0!=0x0):
                oc=outcode0
            else:
                oc=outcode1
                
            if(oc & 0x8):
                x=x0+int((x1-x0)*(ymax-y0)/(y1-y0))
                y=ymax
            elif(oc & 0x4):
                x=x0+int((x1-x0)*(ymin-y0)/(y1-y0))
                y=ymin
            elif(oc & 0x2):
                y=y0+int((y1-y0)*(xmax-x0)/(x1-x0))
                x=xmax
            elif(oc & 0x1):
                y=y0+int((y1-y0)*(xmin-x0)/(x1-x0))
                x=xmin
            if(oc==outcode0):
                x0=x
                y0=y
                outcode0=get_outcode(x0,y0)
            else:
                x1=x
                y1=y
                outcode1=get_outcode(x1,y1)
    if(condition):
        return(x0,y0,x1,y1)



ll=clip(a1,a2,b1,b2)
def draw():                                           
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()                                   
    refresh2d(width, height)                           
    glColor3f(1.0, 1.0, 1.0)                           
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2i(-width//2, 0)
    glVertex2i(width//2, 0)
    glVertex2i(0, -width//2)
    glVertex2i(0, width//2)
    glColor3f(1.0, 1.0, 0)  
    glVertex2i(xmin, ymin)
    glVertex2i(xmax, ymin)
    glVertex2i(xmax, ymin)
    glVertex2i(xmax, ymax)
    glVertex2i(xmax, ymax)
    glVertex2i(xmin,ymax)
    glVertex2i(xmin,ymax)
    glVertex2i(xmin, ymin)
    
    glColor3f(0,1.0, 1.0)       
    glVertex2i(a1,a2)
    glVertex2i(b1,b2)
    x1,y1,x2,y2=ll[0],ll[1],ll[2],ll[3]
    glColor3f(1.0,0, 1.0)       
    glVertex2i(x1,y1)
    glVertex2i(x2,y2)
    glEnd()
	
    glutSwapBuffers()     
    
def refresh2d(width, height):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-width/2, height/2, -width/2, height/2, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    




glutInit()                                             
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width,height)                      
glutInitWindowPosition(500, 10)                           
window = glutCreateWindow("Line clipping")              
glutDisplayFunc(draw)                                  
glutIdleFunc(draw)                                     
glutMainLoop()       
