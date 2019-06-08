from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

elist = []
slst = []
dplist=[]
x0, y0, x1, y1 = 0, 0, 0, 0
def draw_line(x1, y1, x2, y2):
    if(x1>x2):
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    vertical = 0
    m=0
    try:
        m=(y2-y1)/(x2-x1)
    except:
        vertical = 1
    if(vertical):
        if(y1>y2):
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        x = x1
        y = y1
        while(y < y2):
            y += 1
            glBegin(GL_POINTS)
            glVertex2f(x,y)
	    elist.append([x, y])
            glEnd()
            glutSwapBuffers()   
            glFlush()
            time.sleep(0.01)
    elif(m>=0 and m<=1):
        a = y2 - y1
        b = x1 - x2
        d = a + (b / 2)
        x = x1
        y = y1
        while(x < x2):
            if(d<0):
                d += a
            else:
                d += a+b
                y += 1
            x += 1
            glBegin(GL_POINTS)
            glVertex2f(x,y)
            glEnd()
	    elist.append([x, y])
            glutSwapBuffers()   
            glFlush()
            time.sleep(0.01)
    elif(m<=0 and m>=-1):
        y1 = -y1
        y2 = -y2
        a = y2 - y1
        b = x1 - x2
        d = a + (b / 2)
        x = x1
        y = y1
        while(x < x2):
            if(d<0):
                d += a
            else:
                d += a+b
                y += 1
            x += 1
            glBegin(GL_POINTS)
            glVertex2f(x,-y)
            glEnd()
            elist.append([x, -y])
	    glutSwapBuffers()   
            glFlush()
            time.sleep(0.01)
    elif(m>1):
        x1,y1 = y1,x1
        x2,y2 = y2,x2
        a = y2 - y1
        b = x1 - x2
        d = a + (b / 2)
        x = x1
        y = y1
        while(x < x2):
            if(d<0):
                d += a
            else:
                d += a+b
                y += 1
            x += 1
            glBegin(GL_POINTS)
            glVertex2f(y,x)
            glEnd()
	    elist.append([y, x])
            glutSwapBuffers()   
            glFlush()
            time.sleep(0.01)
    elif(m<-1):
        x1,y1 = -y1,x1
        x2,y2 = -y2,x2
        a = y2 - y1
        b = x1 - x2
        d = a + (b / 2)
        x = x1
        y = y1
        while(x < x2):
            if(d<0):
                d += a
            else:
                d += a+b
                y += 1
            x += 1
            glBegin(GL_POINTS)
            glVertex2f(y,-x)    
            glEnd()
	    elist.append([y, -x])
            glutSwapBuffers()   
            glFlush()
            time.sleep(0.01)

def draw_polygon():
    p = int(input("Enter Number of Points "))
    la,lb,a,b,sa,sb=0,0,0,0,0,0
    for i in range(p):
      a,b = map(int, sys.stdin.readline().split())
      dplist.append([a+300,b+300])
      if i:
	draw_line(la + 300, lb + 300, a + 300, b + 300)
      else:
        sa=a
        sb=b
      la=a
      lb=b
    draw_line(la + 300, lb + 300, sa + 300, sb + 300)
      
def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_axes():
    glBegin(GL_LINES)
    glVertex2f(301, 0)   
    glVertex2f(301, 600)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0, 301)   
    glVertex2f(600, 301)
    glEnd()

w, h = 600, 600

def fill_polygon():
	x=0
	y=0
	for i in elist:
		x=i[0]+1
		y=i[0]+1
		break
	while y<600:
		lambd= False
		x=0
		while x<600:
			temp=[x,y]
			t2=[x+1,y]
			if temp in elist and t2 in elist:
				break
			if temp in elist:
				if lambd == True:
					lambd=False
				else:
					lambd=True
			if lambd == True:
				glBegin(GL_POINTS)
				glVertex2f(x,y)
				glEnd()
			x+=1
		y+=1

def draw():                                            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    refresh2d(600, 600)
    glColor3f(1.0, 0.0, 0.0)    
    draw_axes()
    glColor3f(1.0, 0.0, 1.0)    
    draw_polygon()
    glColor3f(0.0, 1.0, 1.0)    
    fill_polygon()
    glutSwapBuffers()   
    glFlush()

glutInit(sys.argv)                                             
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(600, 600)                      
glutInitWindowPosition(0, 0)       
window = glutCreateWindow("Scan line Polygon Filling")              
glutDisplayFunc(draw)                                  
glutIdleFunc(draw)                                     
glutMainLoop()
