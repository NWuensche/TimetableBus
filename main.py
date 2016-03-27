#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Monitor
import time

def main():

    # show bus lines every 30 seconds
    while True:
        Monitor.print_buses()
        time.sleep(30)

if __name__ == '__main__':
    main()
