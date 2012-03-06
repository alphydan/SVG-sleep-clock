from svgfig import *
from math import *
import datetime as dti
from time import strptime


##### Parametric equation of Circle ####
################
# x = r cos(t) #
# y = r cos(t) #
################

nowtime=dti.datetime.now()

def TimeToCoordinates(dtime, option2412=24, radius=3):
    """
    Converts a datetime object to coordinates on the clock
    Arguments:
    - `dtime`: a date time object of the form '2012-02-12 18:56:17.977235'
    - `option2412`:
    it can be accessed with dtime.year, dtime.month, dtime.hour, etc.
    """
    if type(dtime) is not dti.datetime:
        raise TypeError('arg must be a datetime, not a %s' % type(dtime))
    else:
        if option2412==24:
            decimalhour=dtime.hour+dtime.minute/60.0 #convert minutes to decimal 14h30 would be 14.5
            angle= (pi/2)-(decimalhour*2*pi/24)  # transform the hour into an angle
            coordinates=[radius*cos(angle), radius*sin(angle)] #turn angle to coordinates
            return coordinates

        elif option2412==12:
            decimalhour=dtime.hour+dtime.minute/60.0
            if decimalhour<12:
                angle= (decimalhour*2*pi/12)+(pi/2)
                coordinates=[radius*cos(angle), radius*sin(angle)]
            elif decimalhour>=12:
                angle= (decimalhour*2*pi/12)+(pi/2)
                coordinates=[radius*cos(angle), radius*sin(angle)]
            return coordinates

        else:
            print 'use the function as TimeToCoordinates(datetime.datetime object, 24 or 12)'
    

sometime = "2005-12-06T20:10:14"
somedatetime = dti.datetime(*strptime(sometime, "%Y-%m-%dT%H:%M:%S")[0:6])
print somedatetime
# dti.datetime(2005, 12, 6, 12, 13, 14)


        
    


coordsnow=TimeToCoordinates(somedatetime,24)
print coordsnow, '\n', nowtime


mycleverticks={}
for i in range(2,24,4):
    mycleverticks[2*pi/24*i]=i

# mycleverticks[0]="midnight"
# mycleverticks[pi]="noon"

piticks=[2*pi*i/12 for i in range(1,12)]
pi_mini_ticks=[2*pi*i/48 for i in range(1,48)]    

mi_circle_axis=CurveAxis("-3*cos(t+pi/2),3*sin(t+pi/2)", 0, 2*pi-0.08, \
                         arrow_end="myfinalarrow",\
                         # ticks= [1,2,3,4,5,6],\
                         ticks=piticks, labels=False,\
                         miniticks=False)
mi_circle_axis.text_start =-6 #how far away from the circle is the tic-text?
mi_circle_axis.text_angle = 90 #orientation of the hour legend


inner_circle_axis=CurveAxis("-2.8*cos(t+pi/2),2.8*sin(t+pi/2)", 0, 2*pi-0.05, \
                            ticks=pi_mini_ticks, labels=False,
                         miniticks=False)



### Using the Poly Class from SVGFIG
# Poly(d, mode, loop, attribute=value)
# d=[(x,y), (x,y), ...]
# mode, "lines", "bezier", "velocity", "foreback", "smooth", or an abbreviation
# loop, if True, connect the first and last point, closing the loop
thepoly=Poly([(0,0), (coordsnow[0], coordsnow[1]), (0,3)], "lines", True)





away_from_axis=0.3
midnight_label=Text(0,3+away_from_axis,'Midnight')
noon_label=Text(0,-3-2*away_from_axis,'Noon')
six_label=Text(3+2*away_from_axis,0,'6')
nine_label=Text(3+2*away_from_axis,0,'6')
six_label=Text(3+2*away_from_axis,0,'6')
AM_LABEL= Text(1, 0, 'AM')
PM_LABEL= Text(-1, 0, 'PM')
NOW_Label=Text(coordsnow[0], coordsnow[1], 'NOW!')
# label options
# <Text 'Midnight' at (0, 3.3) {'stroke': 'none', 'font-size': 5, 'fill': 'black'}>


mywin = window(-4, 4, -4, 4, x=0, width=100)
Fig(inner_circle_axis, mi_circle_axis,
    midnight_label, noon_label, six_label, AM_LABEL, PM_LABEL, NOW_Label,
    thepoly,
    trans=mywin).SVG().inkview()








# #angle_axis.text_angle = 180 #orientation of the hour legend
# #angle_axis.ticks = [x*4 for x in range(6)]
# #angle_axis.labels = lambda x: "%g" %  x #(x*180/pi)
# #angle_axis.miniticks = [x/2 for x in range(48)]


# # Fig(Fig(angle_axis,trans="x*cos(y/pi), x*sin(y/pi)" )).SVG(window(-60, 100, -60, 40)).inkview()

# # Fig(Fig(angle_axis,trans="x*cos(y), x*sin(y)" ),global_center,local_center).SVG(window(-100, 100, -100, 100)).inkview()
# Fig(Fig(angle_axis, ),global_center,local_center).SVG(window(-100, 100, -100, 100)).inkview()
# # Fig(Fig(angle_axis, )).SVG(window(-6, 100, -6, 40)).inkview()


