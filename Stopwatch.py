"""
This program is a class that creates the functionality of a stopwatch, its primary usage is for
timing the duration of a particular process within a program.
"""

from datetime import datetime
from datetime import timedelta

class Stopwatch(object):
    def __init__(self):
        self._start_time = None
        self._end_time = None
        self._paused = False
        self._pause_before = None
        self._total_pauses = timedelta()
    
    def StartTime(self):
        self._start_time = datetime.now()
        self._end_time = None
        self._paused = False
        self._pause_before = None
    
    def StopTime(self):
        self._end_time = datetime.now()
    
    def GetTime(self):
        if self._end_time != None and self._start_time != None:
            print("Time difference: {}".format((self._end_time - self._start_time) - self._total_pauses))
        else:
            print("Timer hasn't stopped.")

    def PauseTimer(self):
        if self._start_time != None and self._end_time != None and self._paused != True:
            self._pause_before = datetime.now()
            self._paused = True
    
    def UnpauseTimer(self):
        if self._start_time != None and self._end_time != None and self._paused == True:
            self._paused = False
            self._total_pauses += datetime.now() - self._start_time
    
