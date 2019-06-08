from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
x0, y0, x1, y1 = 0, 0, 0, 0
wid,ht=800,800
def make_circle():
    x=0
    y=radius
    d=1-radius
    glBegin(GL_POINTS)
    glVertex2f(x+x0+(wid/2),y+y0+(ht/2))   
    glVertex2f(-x+x0+(wid/2),-y+y0+(ht/2))      
    glVertex2f(-x+x0+(wid/2),y+y0+(ht/2))      
    glVertex2f(x+x0+(wid/2),-y+y0+(ht/2)) 
    glVertex2f(y+x0+(wid/2),x+y0+(ht/2))      
    glVertex2f(y+x0+(wid/2),-x+y0+(ht/2))      
    glVertex2f(-y+x0+(wid/2),x+y0+(ht/2))      
    glVertex2f(-y+x0+(wid/2),-x+y0+(ht/2))    
    glEnd()  
    while(x<y):
       if (d<0):
           x+=1
           d=d+2*x+1
       else:
           x+=1
           y-=1
           d=d+2*x-2*y+1 
       glBegin(GL_POINTS)
       glVertex2f(x+x0+(wid/2),y+y0+(ht/2))   
       glVertex2f(-x+x0+(wid/2),-y+y0+(ht/2))      
       glVertex2f(-x+x0+(wid/2),y+y0+(ht/2))      
       glVertex2f(x+x0+(wid/2),-y+y0+(ht/2)) 
       glVertex2f(y+x0+(wid/2),x+y0+(ht/2))      
       glVertex2f(y+x0+(wid/2),-x+y0+(ht/2))      
       glVertex2f(-y+x0+(wid/2),x+y0+(ht/2))      
       glVertex2f(-y+x0+(wid/2),-x+y0+(ht/2))  
       glEnd()  
       glFlush()         
def makeregion(wid, ht):
    glViewport(0,0,wid,ht)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,wid,0,ht,0.0,1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
def axes():
	glBegin(GL_LINES)
	glVertex2f(wid/2,0)
	glVertex2f(wid/2,ht)
	glVertex2f(0,ht/2)
	glVertex2f(ht,ht/2)
	glEnd()
def drawcircle():                                            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()                                   
    makeregion(wid, ht)                            
    glColor3f(0.0,1.0,0.0)    
    axes()  
    glColor3f(1.0,1.0,1.0)    
    glBegin(GL_POINTS)
    glVertex2f(x0+(wid/2),y0+(ht/2))
    glEnd()  
    glColor3f(1.0,0.0,1.0)    
    make_circle()       
    glutSwapBuffers()
    glFlush()
print('Enter the Center: ')
x0=int(input())
y0=int(input())
x0 = 0 + (x0 - 0) * (800 / float(1500))
y0 = 0 + (y0 - 0) * (800 / float(1500))
print "View Port Center Coordinates: ",x0,y0
radius=int(input('Enter the Radius: '))
glutInit()                                             
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(wid, ht)                      
glutInitWindowPosition(0,0)       
window=glutCreateWindow("Cricle")              
glutDisplayFunc(drawcircle)                                  
glutIdleFunc(drawcircle)                                     
glutMainLoop()  
