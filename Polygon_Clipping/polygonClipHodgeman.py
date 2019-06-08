from __future__ import division
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import copy


window = 0                                             
width, height = 600,600                     
vertex_list=[]
orig=[]
n=int(raw_input("Enter no. of points for polygon: "))
for i in range(0,n):
	a1,a2=map(int,raw_input("Enter (x,y) coordinates : ").split())
	vertex_list.append([a1,a2])
	orig.append([a1,a2])

xmin,ymin,xmax,ymax=map(int,raw_input("Enter xmin , ymin , xmax , ymax forclip window : ").split())

def inside(v,j):
    if(j==0):
        if(v[0]<xmin):
            return False
    elif(j==1):
        if(v[0]>xmax):
            return False
    elif(j==2):
        if(v[1]<ymin):
            return False
    else:
        if(v[1]>ymax):
            return False
    return True


def intersection(v1,v2,j):
    if(j==0):
        y=v1[1]+int((v2[1]-v1[1])/(v2[0]-v1[0])*(xmin-v1[0]))
        return([xmin,y])
    elif(j==1):
        y=v1[1]+int((v2[1]-v1[1])/(v2[0]-v1[0])*(xmax-v1[0]))
        return([xmax,y])
    elif(j==2):
        x=v1[0]+int((v2[0]-v1[0])/(v2[1]-v1[1])*(ymin-v1[1]))
        return([x,ymin])
    elif(j==3):
        x=v1[0]+int((v2[0]-v1[0])/(v2[1]-v1[1])*(ymax-v1[1]))
        return([x,ymax])

def clip(vertex_list):
    new_vertex_list=[]
    for j in range(0,4):
        for i in range(0,len(vertex_list)):
            v1=vertex_list[i]
            v2=vertex_list[(i+1)%len(vertex_list)]
            if(inside(v1,j)):      
                if(inside(v2,j)):
                    if(v2 not in new_vertex_list):
                        new_vertex_list.append(v2)
                else:               
                    temp=intersection(v1,v2,j)
                    if(temp not in new_vertex_list):
                        new_vertex_list.append(temp)
            else:
                if(inside(v2,j)):   
                    temp=intersection(v1,v2,j)
                    if(temp not in new_vertex_list):
                        new_vertex_list.append(temp)
                    if(v2 not in new_vertex_list):
                        new_vertex_list.append(v2)
                else:               
                    pass
        
        vertex_list=[]
        vertex_list=copy.deepcopy(new_vertex_list)
        new_vertex_list=[]
    #print(vertex_list)
    return(vertex_list)


ll=clip(vertex_list)


def draw():                                            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()                                   
    refresh2d(width, height)                           
    glColor3f(1.0, 1.0, 1.0)                           
    glLineWidth(2)
    glClearColor (1,1,1,1);
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
    global orig,ll
    glColor3f(0,1.0, 1.0)
    
    for i in range(0,len(orig)):
    	glVertex2i(orig[i][0], orig[i][1])
    	glVertex2i(orig[(i+1)%len(orig)][0],orig[(i+1)%len(orig)][1])
    glColor3f(1.0,0, 1.0)  
    
    for i in range(0,len(ll)):
    	glVertex2i(ll[i][0], ll[i][1])   
    	glVertex2i(ll[(i+1)%len(ll)][0],ll[(i+1)%len(ll)][1])  
    
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
window = glutCreateWindow("Polygon Clipping")              
glutDisplayFunc(draw)                                 
glutIdleFunc(draw)                                     
glutMainLoop()       
