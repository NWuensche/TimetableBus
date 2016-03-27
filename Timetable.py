import json
import urllib.request
import ast

def get_list():
    url = 'http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort=Dresden&hst=CasparDavidFriedrichStra%C3%9Fe'
    response = urllib.request.urlopen(url)
    data_raw = response.read()
    data_utf = data_raw.decode("utf-8")
    data_list = ast.literal_eval(data_utf)
    return data_list

def get_first_buses(data_list):
    next_buses = []
    for ride in data_list:
        if ride[0] not in [next_ride[0] for next_ride in next_buses]:
            next_buses.append(ride)
    return next_buses

def get_buses():
    return get_first_buses(get_list())
