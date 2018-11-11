import math

#distline takes a point, and a line defined by two points, and calculates both the minimimum distance from the point to the line, and the point where it intersects the line
#x0,y0 are the coordinates of your starting location, and ax,ay and bx,by are the coordinates of the endpoints of your line
def distline(x0,y0,ax,ay,bx,by):
    m = (by-ay)/(bx-ax)
    print m
    solx = (-(ay-y0)+m*ax+x0/m)/(m+1/m)
    soly=ay+m*(solx-ax)
    print solx
    print soly
    if solx>max(ax,bx):
        solx=max(ax,bx)
    if soly>max(ay,by):
        solx=max(ay,by)
    if solx<min(ax,bx):
        solx=min(ax,bx)
    if soly<min(ay,by):
        solx=min(ay,by)
    return [solx,soly,math.sqrt((solx-x0)**2+(soly-y0)**2)]

print distline(-2.0,0.0,0.0,-1.0,1.0,0.0)
