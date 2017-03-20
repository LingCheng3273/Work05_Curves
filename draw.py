from display import *
from matrix import *
import math


def add_circle( points, cx, cy, cz, r, step ):
    r= float(r)
    cx= float(cx)
    cy= float(cy)
    cz= float(cz)
    initX= cx
    initY= cy
    initZ= cz
    step= 50
    steps_taken= 0.0
    while steps_taken < 1:
        rad = 2*math.pi*steps_taken
        rad_next = 2*math.pi*(steps_taken-1.0/step)
        add_edge(points, r*math.cos(rad)+cx, r*math.sin(rad)+cy, cz, r*math.cos(rad_next)+cx, r*math.sin(rad_next)+cy, cz)
        steps_taken= steps_taken+ (1.0 / step)
    add_edge(points, r*math.cos(rad)+cx, r*math.sin(rad)+cy, cz, r*math.cos(0.0)+initX, r*math.sin(0)+initY, initZ)

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    steps_taken= 0.0
    xCoef= generate_curve_coefs(x0, x1, x2, x3, curve_type)
    yCoef= generate_curve_coefs(y0, y1, y2, y3, curve_type)
    print "this is xCoef:"
    print xCoef
    print "this is yCoef:"
    print yCoef
    while steps_taken < 1:
        next_step= steps_taken + 1.0/step
        x= float(xCoef[0])* math.pow(steps_taken, 3)+ float(xCoef[1])* math.pow(step_taken, 2) + float(xCoef[2])* step_taken + float(xCoef[3])
        y= float(yCoef[0])* math.pow(steps_taken, 3)+ float(yCoef[1])* math.pow(step_taken, 2) + float(yCoef[2])* step_taken + float(yCoef[3])
        x_next= float(xCoef[0])* math.pow(next_step, 3)+ float(xCoef[1])* math.pow(next_step, 2) + float(xCoef[2])* next_step + float(xCoef[3])
        y_next= float(yCoef[0])* math.pow(next_step, 3)+ float(yCoef[1])* math.pow(next_step, 2) + float(yCoef[2])* next_step + float(yCoef[3])
        add_edge(points, x, y, 0, x_next, y_next, 0)
        steps_taken = steps_taken + 1.0/ step
    add_edge(points, x, y, 0, xCoef[3], yCoef[3], 0)

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return
    
    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )
    



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
