#!/usr/bin/env python3

import argparse
import datetime
import sys

import unspot

argument_parser = argparse.ArgumentParser(prog=unspot.__name__, description='Unspot Command line interface')
argument_parser.add_argument('-u', '--unspot-url', required=True, type=str)
argument_parser.add_argument('-t', '--authorization-token', required=True, type=str)
argument_parser.add_argument('-d', '--desk-id', required=True, type=str)
argument_parser.add_argument('-s', '--start-timestamp', type=int)
argument_parser.add_argument('-e', '--end-timestamp', type=int)
arguments = argument_parser.parse_args()

if (arguments.start_timestamp is None) or (argument_parser.end_timestamp is None):
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    arguments.start_timestamp = int(datetime.datetime(tomorrow.year,
                                                      tomorrow.month,
                                                      tomorrow.day,
                                                      hour=10,
                                                      minute=0,
                                                      second=0).timestamp())
    dayAfterTomorrow = tomorrow + datetime.timedelta(days=1)
    arguments.end_timestamp = int(datetime.datetime(dayAfterTomorrow.year,
                                                    dayAfterTomorrow.month,
                                                    dayAfterTomorrow.day,
                                                    hour=0,
                                                    minute=0,
                                                    second=0).timestamp())

connection = unspot.Connection(arguments.unspot_url)
response = connection.send_request(unspot.BookDeskRequest(arguments.authorization_token,
                                                          arguments.desk_id,
                                                          arguments.start_timestamp,
                                                          arguments.end_timestamp))
print(response)
sys.exit(0 if response else 1)
