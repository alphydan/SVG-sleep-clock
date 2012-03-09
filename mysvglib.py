#!/usr/bin/env python

"""mysvglib.py: Some functions for https://github.com/alphydan/SVG-sleep-clock."""

##### Import Statements #####
from svgfig import *
from math import *
import datetime as dti
from time import strptime


##### Parametric equation of Circle ####
   ################
   # x = r cos(t) #
   # y = r cos(t) #
   ################

def time_to_coordinates(dtime, option2412=24, radius=3):
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
            coordinates=(radius*cos(angle), radius*sin(angle)) #turn angle to coordinates
            return coordinates

        elif option2412==12:
            decimalhour=dtime.hour+dtime.minute/60.0
            if decimalhour<12:
                ##### THIS DOES NOT WORK YET!! ######
                angle= (decimalhour*2*pi/12)+(pi/2)
                coordinates=(radius*cos(angle), radius*sin(angle))
            elif decimalhour>=12:
                ##### THIS DOES NOT WORK YET!! ######
                angle= (decimalhour*2*pi/12)+(pi/2)
                coordinates=(radius*cos(angle), radius*sin(angle))
            return coordinates

        else:
            print 'use the function as TimeToCoordinates(datetime.datetime object, 24 or 12)'



def create_clock_skeleton(lang='en'):
    """
    creates axis, ticks, numbers, labels
    """
    
    piticks=[2*pi*i/12 for i in range(1,12)]
    pi_mini_ticks=[2*pi*i/48 for i in range(1,48)]    
    outer_circle_axis=CurveAxis("-3*cos(t+pi/2),3*sin(t+pi/2)", 0, 2*pi-0.08, \
                         arrow_end="myfinalarrow",\
                         # ticks= [1,2,3,4,5,6],\
                         ticks=piticks, labels=False,\
                         miniticks=False)
    outer_circle_axis.text_start =-6 #how far away from the circle is the tic-text?
    outer_circle_axis.text_angle = 90 #orientation of the hour legend


    inner_circle_axis=CurveAxis("-2.8*cos(t+pi/2),2.8*sin(t+pi/2)", 0, 2*pi-0.05, \
                            ticks=pi_mini_ticks, labels=False,
                         miniticks=False)
    away_from_axis=0.3


    # bigger labels
    eighteen_label=Text(-3-2*away_from_axis,0,'18')
    eighteen_label.attr['font-size']='7'
    eighteen_label.defaults['font-size']='7'
    six_label=Text(3+2*away_from_axis,0,'6')
    if lang=='es':
        midnight_label=Text(0,3+away_from_axis,'Medianoche')
        noon_label=Text(0,-3-2*away_from_axis,'Mediodia')
    elif lang=='en':
        midnight_label=Text(0,3+away_from_axis,'Midnight')
        noon_label=Text(0,-3-2*away_from_axis,'Noon')
    elif lang=='fr':
        midnight_label=Text(0,3+away_from_axis,'Minuit')
        noon_label=Text(0,-3-2*away_from_axis,'Midi')
    else:
        print 'please give input as "es", "en" or "fr"'

    # smaller labels
    three_label=Text(2.5,2.5,'3')
    three_label.defaults['font-size']='5'
    nine_label=Text(2.5,-2.5,'9')
    fifteen_label=Text(-2.5,-2.5,'15')
    twenty1_label=Text(-2.5,2.5,'21')


    print eighteen_label.attr
    AM_LABEL= Text(1, 0, 'AM')
    PM_LABEL= Text(-1, 0, 'PM')
    # NOW_Label=Text(coordsnow[0], coordsnow[1], 'NOW!')
# label options
# <Text 'Midnight' at (0, 3.3) {'stroke': 'none', 'font-size': 5, 'fill': 'black'}>

    

    mywin = window(-4, 4, -4, 4, x=0, width=100)
    fig_skeleton=Fig(inner_circle_axis, outer_circle_axis,
        AM_LABEL, PM_LABEL, # NOW_Label,
        midnight_label, noon_label, six_label, eighteen_label,
        three_label, fifteen_label, nine_label, twenty1_label,
#        thepoly,
        trans=mywin) #.SVG().inkview()

    return fig_skeleton


def arc_between_times(ini_datetime,final_datetime):
    """ Creates a tuple with the points that define the arc of a circle
    between two times.  It does some sanity checks along the way.
    
    Arguments:
    - `ini_datetime`:  Initial datetime
    - `final_datetime`: Final datetime (has to be within 24h of Initial datetime, and greater)
    """
    dadelta=dti.timedelta(0,0,0,0,5,0) # a time-delta of 5mn

    #################
    # Sanity Checks #
    #################

    # are they datetime objects?
    assert type(ini_datetime)==dti.datetime, 'Type Error: \n input %s has to be python datetime.datetime object' % str(ini_datetime)
    assert type(final_datetime)==dti.datetime, 'Type Error: \n input %s has to be python datetime.datetime object' % str(ini_datetime)

    # are they more than 5mn appart?
    full_interval= final_datetime-ini_datetime
    minutes_appart=(full_interval.seconds)/60.0 #minutes between the two

    if minutes_appart==0:
        print 'your times are less than 1mn appart.  Please chose a different pair of times'
    if minutes_appart<=5:
        return [(0,0), time_to_coordinates(ini_datetime), time_to_coordinates(final_datetime)]
    elif minutes_appart>5:
        print 'more than 5'
    

    

def create_chese_slice(datetime1,datetime2, phase):
    """Creates the shape of the arc of a circle between two times
    the circle is approximated with 5mn intervals
    Arguments:
    - `datetime1`: datetime object
    - `datetime2`: datetime object
    - `phase`: Awake, Sleep, REM, light
    """
    
skeleton=create_clock_skeleton('es')
# skeleton.SVG().inkview()

tt1=dti.datetime(16,12,30,9,0,0)
tt2=dti.datetime(16,12,30,9,0,0)
danow=dti.datetime.now()
coor=time_to_coordinates(tt1)
print coor

dadelta=dti.timedelta(0,0,0,0,5,0) # a time-delta of 5mn

print tt1, danow
print tt1+dadelta, danow+dadelta
print tt1+2*dadelta, danow+10*dadelta

thearc=arc_between_times(tt1, tt2)
print thearc


