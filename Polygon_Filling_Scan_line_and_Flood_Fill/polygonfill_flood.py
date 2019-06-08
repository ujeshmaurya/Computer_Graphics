from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

elist = []
plst = []
slst = []
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
	t1 =0
	t2 =0
	for i in elist:
		t1=i[0]
		t2=i[1]
		break
	slst.append([t1+1, t2+1])
	while(len(slst) > 0):
		temp=slst.pop()
		plst.append(temp)
  		x=temp[0]
  		y=temp[1]
		glBegin(GL_POINTS)
  		glVertex2f(x, y)
		glEnd()
		#glutSwapBuffers()
		glFlush()
  		a=[x,y+1]
  		a2=[x-1,y+1]
  		b=[x-1,y]
  		b2=[x-1,y-1]
  		c=[x,y-1]
  		c2=[x+1,y-1]
  		d=[x+1,y]
  		d2=[x+1,y+1]
  		if(a not in plst and a not in elist):
  			slst.append(a)
  		if(b not in plst and b not in elist):
  			slst.append(b)
  		if(c not in plst and c not in elist):
  			slst.append(c)
  		if(d not in plst and d not in elist):
  			slst.append(d)

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
window = glutCreateWindow("Polygon Filling")              
glutDisplayFunc(draw)                                  
glutIdleFunc(draw)                                     
glutMainLoop()
