from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
xw, yw, xv, yv= 0, 0, 0, 0   
vwidth, vheight, wwidth, wheight = 0, 0, 0, 0
xwmin, ywmin, xwmax, ywmax, xvmin, yvmin, xvmax, yvmax = 0, 0, 0, 0, 0, 0, 0, 0                    
def viewPort():                                            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glViewport(0, 0, vwidth, vheight)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, vwidth, 0, vheight, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(1.0, 0.0, 0.0)    
    xv = xvmin + (xw - xwmin) * (vwidth / float(wwidth))
    yv = yvmin + (yw - ywmin) * (vheight / float(wheight))
    glBegin(GL_POINTS)                                  
    glVertex2f(xv, yv)                                  
    glEnd()                       
    glutSwapBuffers()   
xwmin=int(input())
ywmin=int(input())
xwmax=int(input())
ywmax=int(input())
xvmin=int(input())
yvmin=int(input())
xvmax=int(input())
yvmax=int(input())
xw=int(input())
yw=int(input())
wwidth=xwmax-xwmin
wheight=ywmax-ywmin
vwidth=xvmax-xvmin
vheight=yvmax-yvmin
glutInit()                                             
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(vwidth, vheight)                      
glutInitWindowPosition(0, 0)                           
window=glutCreateWindow("view tranformation")              
glutDisplayFunc(viewPort)                                  
glutIdleFunc(viewPort)                                     
glutMainLoop()  
