#!/usr/bin/env python

"""mysvglib.py: Some functions for https://github.com/alphydan/SVG-sleep-clock."""

##### Import Statements #####
from svgfig import *
from math import *
import datetime as dti
from time import strptime

###########  This library is to implement the following strategy   ##########
##


class SleepTimeStamp(object):
    """This class describes time stamps with a bunch of possible attributes like:
    `dti`: Datetime object
    `BEM`: begining, end or middle of a time period.
    `phase`: Sleep phase: Undefined(0), Awake(1), REM(2), light(3), deep(4), InBed (5), Snoozing (6).
    `subjective_awareness`: scale from 1 to 10.
    `comment`:
    """
    # attributes
    
    def __init__(self, dti, BEM, phase, subjective_awareness, comment):
        """
        """
        
        




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


##### Parametric equation of Circle ####
   ################
   # x = r cos(t) #
   # y = r cos(t) #
   ################


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



def create_clock_skeleton(lang='en', radius=3):
    """
    creates axis, ticks, numbers, labels
    """
    piticks=[2*pi*i/12 for i in range(1,12)]
    pi_mini_ticks=[2*pi*i/48 for i in range(1,48)]    
    outer_circle_axis=CurveAxis("-%s*cos(t+pi/2),%s*sin(t+pi/2)" % (radius, radius), 0, 2*pi-0.08, \
                         arrow_end="myfinalarrow",\
                         # ticks= [1,2,3,4,5,6],\
                         ticks=piticks, labels=False,\
                         miniticks=False)
    outer_circle_axis.text_start =-6 #how far away from the circle is the tic-text?
    outer_circle_axis.text_angle = 90 #orientation of the hour legend

    #2.8
    inner_circle_axis=CurveAxis("-%s*cos(t+pi/2),%s*sin(t+pi/2)" %(0.93*radius, 0.93*radius), 0, 2*pi-0.05, 
                            ticks=pi_mini_ticks, labels=False,
                         miniticks=False)
    away_from_axis=0.3


    # bigger labels
    eighteen_label=Text(-radius-2*away_from_axis,0,'18')
    eighteen_label.attr['font-size']='7'
    eighteen_label.defaults['font-size']='7'
    six_label=Text(radius+2*away_from_axis,0,'6')
    if lang=='es':
        midnight_label=Text(0,radius+away_from_axis,'Medianoche')
        noon_label=Text(0,-radius-2*away_from_axis,'Mediodia')
    elif lang=='en':
        midnight_label=Text(0,radius+away_from_axis,'Midnight')
        noon_label=Text(0,-radius-2*away_from_axis,'Noon')
    elif lang=='fr':
        midnight_label=Text(0,radius+away_from_axis,'Minuit')
        noon_label=Text(0,-radius-2*away_from_axis,'Midi')
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

    # day separator at mid-day.
    # day_separator=SVG("line", x1=0, y1=0, x2=0, y2=-3)
    day_separator=Line(0, 0, 0, -3, stroke="rgb(190,190,190)", stroke_width=0.5,
                       )  # .SVG(stroke="rgb(163,163,163)") # # .SVG("x, 2*y")

    
#     Poly([(0,0),(0, -radius)], "lines", False, stroke="rgb(163,163,163)", stroke_width=0.5, 'opacity':"10%") # , stroke-opacity:0.3)

# fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1;opacity:0.34156379

    mywin = window(-4, 4, -4, 4, x=0, width=100)
    fig_skeleton=Fig(inner_circle_axis, outer_circle_axis,
        AM_LABEL, PM_LABEL, 
        midnight_label, noon_label, six_label, eighteen_label,
        three_label, fifteen_label, nine_label, twenty1_label,
        day_separator,
#        thepoly,
        trans=mywin).SVG() #.inkview()

    return fig_skeleton


# SVG("g", SVG("rect", x=1, y=1, width=2, height=2), 
#                 SVG("rect", x=3, y=3, width=2, height=2), 
#            id="mygroup", fill="blue")



def arc_between_times(ini_datetime,final_datetime):
    """ Creates a tuple with the points that define the arc of a circle
    between two times.  It does some sanity checks along the way.
    
    Arguments:
    - `ini_datetime`:  Initial datetime
    - `final_datetime`: Final datetime (has to be within 24h of Initial datetime, and greater)
    """


    #################
    # Sanity Checks #
    #################

    # are they datetime objects?
    assert type(ini_datetime)==dti.datetime, 'Type Error: \n input %s has to be python datetime.datetime object' % str(ini_datetime)
    assert type(final_datetime)==dti.datetime, 'Type Error: \n input %s has to be python datetime.datetime object' % str(ini_datetime)

    # count separation.
    full_interval= final_datetime-ini_datetime
    seconds_interval=full_interval.total_seconds()
    minutes_interval=full_interval.total_seconds()/60.0
    hours_interval=minutes_interval/60.0
    
    print '\n', ini_datetime,'-->', final_datetime
    print 'seconds:', seconds_interval
    print 'minutes:', minutes_interval
    print 'hours:', hours_interval

    # are the timedates in the right order?
    if seconds_interval<0:
        print 'Your initial datetime is larger than the final one.  \n Are they reversed?'
        return None
    # are the timedates different?
    elif seconds_interval==0:
        print 'both datimes are the same.  Are your dates and times correct?'
        return None
    # are they less or 5mn appart?
    elif minutes_interval<=5:
        return [(0,0), time_to_coordinates(ini_datetime), time_to_coordinates(final_datetime)]
    elif hours_interval>24:
        print 'the times are more than 24h apart'
        return None
    else: #the hours are between 5mn and 24h apart.
        if final_datetime.hour>12 and ini_datetime.hour<12:
            # If two datetimes have the same date
            #  (day/month/year) but the times are on different
            # sides of mid-day, for ex. 11h and 13h, they belong on different clocks.
            # we would still like to print initial_time -> 12:00
            # and, on another clock 12:00 -> final timeb
            mid_day=dti.datetime(ini_datetime.year, ini_datetime.month, ini_datetime.day, 12,0,0)
            return arc_series(ini_datetime, mid_day)

            print '\n the two times are on the same day, on either side of midday. \n Please try different dates'
        else:
            return arc_series(ini_datetime, final_datetime)
    
def arc_series(ini_datetime, final_datetime):
    """ Creates the points on the arc of circle
    
    Arguments:
    - `ini_datetime`:  Initial datetime
    - `final_datetime`: Final datetime (has to be within 24h of Initial datetime, and greater)
    """
    delta5mn=dti.timedelta(0,0,0,0,5,0) # a time-delta of 5mn
    
    the_coords=[(0,0),time_to_coordinates(ini_datetime)]
    next_time_step=ini_datetime+delta5mn # add 5mn to initial time
    while next_time_step<final_datetime: # while time step is below final time
        the_coords.append(time_to_coordinates(next_time_step))
        next_time_step+=delta5mn # do 5mn increments
        # print next_time_step
    the_coords.append(time_to_coordinates(final_datetime))
    return the_coords


def create_cheese_slice(arc_of_time, sleep_phase=5):
    """Creates the shape of the arc of a circle between two times
    the circle is approximated with 5mn intervals
    Arguments:
    - `datetime1`: datetime object
    - `datetime2`: datetime object
    - `phase`: Undefined(0), Awake(1), REM(2), light(3), deep(4), InBed (5)
    """
    sleep_phase_color={0:"#FFFFFF", 1: "#dddddd", 2: "#ADFF2F", 3: "#E3E3E3", 4: "#292929", 5: "#00EE76"}
    sleep_phase_opacity={0: 1, 1: 0.1, 2: 1, 2: 0.7, 3: 0.8, 4: 0.9, 5: 0.8}
    the_slice=Poly(arc_of_time, "lines", True, stroke="rgb(163,163,163)", stroke_width=0.1,
                   fill=sleep_phase_color[sleep_phase], fill_opacity=sleep_phase_opacity[sleep_phase])
    return the_slice


    



times=[[dti.datetime(2016,11,22,23,0,0), dti.datetime(2016,11,23,2,00,0), 5],
       [dti.datetime(2016,11,23,7,0,0), dti.datetime(2016,11,23,7,30,0), 5],
       [dti.datetime(2016,11,22,12,00,0), dti.datetime(2016,11,22,12,30,0), 5],
       [dti.datetime(2016,11,22,17,00,0), dti.datetime(2016,11,22,17,30,0), 5],
       ]




# print tt1,
# print tt1+dadelta, danow+dadelta
# print tt1+2*dadelta, danow+10*dadelta


skeleton=create_clock_skeleton("fr")
mywin = window(-4, 4, -4, 4, x=0, width=100)


for i in range(4):
    arc=arc_between_times(times[i][0],times[i][1])
    the_slice=create_chese_slice(arc,times[i][2])
    cheese=Fig(the_slice,trans=mywin).SVG()
    skeleton.append(cheese)

skeleton.inkview()

# def create_legend():
#     """Creates a legend with boxes for each color
#     """
#     sleep_phase_color={0:"#FFFFFF", 1: "#dddddd", 2: "#ADFF2F", 3: "#E3E3E3", 4: "#292929", 5: "#00EE76"}
#     sleep_phase_opacity={0: 1, 1: 0.1, 2: 1, 2: 0.7, 3: 0.8, 4: 0.9, 5: 0.8}
#     unknown=SVG("rect", x=10, y=10, width=60, height=60, fill=sleep_phase_color, opacity=sleep_phase_opacity)
#     legend= SVG("rect", x=30, y=30, width=60, height=60, fill="blue")


# create_legend().inkview()


# thearc=arc_between_times(tt1, tt2)
# the_slice=create_chese_slice(thearc,5)


# a=the_slice
# b=skeleton


# cheese=Fig(a,trans=mywin).SVG()
# cheese.append(b)  # to combine different graphs, curves or elements
# cheese.inkview()
# canv=canvas(cheese,canv)
# canv.inkview()
# Fig(the_slice,skeleton).SVG().inkview()


# SVG attributes fill="blue", fill_opacity=0.3, stroke="blue",  stroke="blue", stroke_width=0.5


    # canv = svgfig.canvas(graph, labels, width=w, height=h)
    #     canv.save(filename)



#     fig_skeleton=Fig(inner_circle_axis, outer_circle_axis,
#         AM_LABEL, PM_LABEL, 
#         midnight_label, noon_label, six_label, eighteen_label,
#         three_label, fifteen_label, nine_label, twenty1_label,
#         day_separator,
# #        thepoly,
#         trans=mywin).SVG() #.inkview()
