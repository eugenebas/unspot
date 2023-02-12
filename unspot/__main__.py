#!/usr/bin/env python3
import argparse
import datetime
import sys
import unspot

argument_parser = argparse.ArgumentParser(prog=unspot.__name__, description='Unspot Command line interface')
argument_parser.add_argument('-u', '--unspot-url',
                             required=True,
                             type=str,
                             help='The address which you\'re using to access the Unspot web interface.')
argument_parser.add_argument('-t', '--authorization-token',
                             required=True,
                             type=str,
                             help='Should be retrieved with debugger from any API request in browser.')
argument_parser.add_argument('-d', '--desk-id',
                             required=True,
                             type=str,
                             help='Should be retrieved with debugger from /api/bookings/desk/new POST request.')
argument_parser.add_argument('-s', '--start-timestamp',
                             type=int,
                             help='Not obligatory, default value is tomorrow 10:00 AM.')
argument_parser.add_argument('-e', '--end-timestamp',
                             type=int,
                             help='Not obligatory, default value is tomorrow 12:00AM.')
arguments = argument_parser.parse_args()

if arguments.start_timestamp is None:
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    arguments.start_timestamp = int(datetime.datetime(tomorrow.year,
                                                      tomorrow.month,
                                                      tomorrow.day,
                                                      hour=10,
                                                      minute=0,
                                                      second=0).timestamp())
if arguments.end_timestamp is None:
    dayAfterTomorrow = datetime.date.today() + datetime.timedelta(days=2)
    arguments.end_timestamp = int(datetime.datetime(dayAfterTomorrow.year,
                                                    dayAfterTomorrow.month,
                                                    dayAfterTomorrow.day,
                                                    hour=0,
                                                    minute=0,
                                                    second=0).timestamp())


connection = unspot.Connection(arguments.unspot_url)
response = connection.send(unspot.BookDeskRequest(arguments.authorization_token,
                                                  arguments.desk_id,
                                                  arguments.start_timestamp,
                                                  arguments.end_timestamp))
print(response)
sys.exit(0 if response else 1)
