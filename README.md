# Connect Raspberry Pi and Android
A program to send data from RasPi to Android Phone and vice versa
## How to use
### Send data from RasPi to Android
1. Then you have to install InstaPush on your Phone and create an account
2. After that, you have to add the password and Usernames whereever is a Sensible.<Name> in the main.py. You don't have to import Sensible, that is a file where I'm storing the passwords
3. Try to run it. It should send you a bus timetable to your phone.

### Send data from Android to RasPi
1. first off, you have to install the Todoist API on your RasPi

    ``` bash
    pip install todoist
    ```

2. Change the API stuff to the username and password of yours
3. Download Todoist onto your phone
4. Send messages to the RasPi in the form of the username of your Todoist Account, e.g. set your username to bus to get a bus timetable
