#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import pycurl, json
import Timetable
#import todoist
from pytodoist.api import TodoistAPI
import Sensitive

from io import BytesIO as StringIO
app_ID = Sensitive.app_ID
app_secret = Sensitive.app_secret
pushEvent = "message"
pushMessage = "first"
buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://api.instapush.im/v1/post')
c.setopt(c.HTTPHEADER, ['x-instapush-appid: ' + app_ID,
'x-instapush-appsecret: ' + app_secret,
'Content-Type: application/json'])

#todoist
#api = todoist.TodoistAPI()
api = TodoistAPI()
user = api.login(Sensitive.e_mail, Sensitive.password)
user_info = user.json()
#response = api.sync(recource_types = ['all'])
pushMessage = user_info['full_name']



# create a dictionary structure for the JSON data to post to Instapush
json_fields = {}

# setup JSON values
json_fields['event']=pushEvent
json_fields['trackers'] = {}
json_fields['trackers']['message']=pushMessage

postfields = json.dumps(json_fields)

# make sure to send the JSON with post
c.setopt(c.POSTFIELDS, postfields)

# set this so we can capture the resposne in our buffer
c.setopt(c.WRITEFUNCTION, buffer.write)

# uncomment to see the post that is sent
#c.setopt(c.VERBOSE, True)
def change_push_message(pushMessage):
    json_fields['trackers']['message']=pushMessage
    postfields = json.dumps(json_fields)
    c.setopt(c.POSTFIELDS, postfields)

def do_what_user_wants():
    user = api.login(Sensitive.e_mail, Sensitive.password)
    user_info = user.json()
    input_str = user_info['full_name']
    input_tokens = input_str.split()
    if input_tokens[0] == 'bus':
        pushMessage = ''
        start = "CasparDavidFriedrichStraße" # default value
        if len(input_tokens) > 1:
        	start = input_tokens[1]
        rides = Timetable.get_list(start)

#        rides = Timetable.get_buses(start)
        print(rides)
        for ride in rides:
            pushMessage += "{line} to {destination}: {time}Min, \n"\
                .format(line = ride[0], destination = ride[1], time = ride[2])

        pushMessage = pushMessage[:-3] # delete last comma
        change_push_message(pushMessage)
        c.perform()
        print("Message sent!\n")

def start_message():
    change_push_message("RasPi started!")
    c.perform()


# setup an indefinite loop that looks for the door to be opened / closed
def main():
    start_message()
    while True:
        body= buffer.getvalue()
        do_what_user_wants() # look for username
        # reset the buffer
        buffer.truncate(0)
        buffer.seek(0)
        time.sleep(15)

    c.close()

if __name__ == '__main__':
    main()
