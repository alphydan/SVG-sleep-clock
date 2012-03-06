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


def create_clock_skeleton():
    """
    creates axis, ticks, numbers, labels
    """
    

