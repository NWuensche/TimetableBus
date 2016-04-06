# -*- coding: utf-8 -*-
import json
from urllib2 import Request as request
import urllib2
import ast

# get the bus lines from the website and parse it to a list
def get_list(start):
#    url = 'http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort=Dresden&hst=CasparDavidFriedrichStra%C3%9Fe'
    url = 'http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort=Dresden&hst=' + start
    req = request(url)
    response = urllib2.urlopen(req)
    data_raw = response.read()
    data_utf = data_raw.decode("utf-8")
    data_list = ast.literal_eval(data_utf)
    return data_list

# just store the first time a bus comes
def get_first_buses(data_list):
    next_buses = []
    for ride in data_list:
        if ride[0] not in [next_ride[0] for next_ride in next_buses]:
            next_buses.append(ride)
    return next_buses

# return the first times, a bus line comes
def get_buses(start):
    return get_first_buses(get_list(start))
