#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import pycurl, json
import Timetable
import todoist
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


# setup an indefinite loop that looks for the door to be opened / closed
def main():
	while True:
		body= buffer.getvalue()
		# reset the buffer
		buffer.truncate(0)
		buffer.seek(0)
		time.sleep(15)
		
	c.close()

if __name__ == '__main__':
	main()
