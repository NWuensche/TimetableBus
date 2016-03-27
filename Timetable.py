import json
import urllib.request
import ast

def get_data():
    url = 'http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort=Dresden&hst=CasparDavidFriedrichStra%C3%9Fe'
    response = urllib.request.urlopen(url)
    data_raw = response.read()
    data_utf = data_raw.decode("utf-8")
    data_list = ast.literal_eval(data_utf)
    return data_list
