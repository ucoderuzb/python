# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 22:46:05 2022

@author: User
"""

import datetime as dt

now = dt.datetime.now()
newyear = dt.datetime(2023, 1, 1, 00, 00, 00)
dif = newyear - now
minute = int((dif.seconds/60)%60)
hour = int(dif.seconds/3600)
second = int(dif.seconds - (hour * 3600) - (minute * 60))
allseconds = ((dif.days * 86400) + (hour * 3600) + (minute * 60) + second)
allminute = ((dif.days * 1440) + (hour * 60) + minute)
allhour = ((dif.days * 24) + hour)
sentence = f"Yangi yilga {dif.days} kun {hour} soat {minute} minut {second} sekund qoldi.\nBu degani jami {allseconds} sekund, {allminute} minut, {allhour} soat qoldi degani"
print(sentence)
birthday = dt.datetime(2022, 4, 30, 00, 00)
dif2 = birthday - now
minute2 = int((dif.seconds/60)%60)
hour2 = int(dif.seconds/3600)
second2 = int(dif.seconds - (hour * 3600) - (minute * 60))
allseconds2 = ((dif2.days * 86400) + (hour2 * 3600) + (minute2 * 60) + second2)
allminute2 = ((dif2.days * 1440) + (hour2 * 60) + minute2)
allhour2 = ((dif2.days * 24) + hour2)
sentence2 = f"Tug'ilgan kuningizga {dif2.days} kun {hour2} soat {minute2} minut {second2} sekund qoldi.\nBu degani jami {allseconds2} sekund, {allminute2} minut, {allhour2} soat qoldi degani"
print(sentence2)