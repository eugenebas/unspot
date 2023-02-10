from .request import Request
import json


class BookDeskRequest(Request):
    def __init__(self, authorization_token, desk_id, start_timestamp, end_timestamp):
        request = {
            'title': 'title',
            'desk': desk_id,
            'organizer': None,
            'guest': None,
            'force': False,
            'sendNotification': False,
            'timeRanges': [{'startDate': start_timestamp,
                            'endDate': end_timestamp}],
            'isBookingByQr': False,
            'placeFrom': 'MAP'
        }
        body = json.dumps(request).encode('utf-8')
        super().__init__('/api/bookings/desk/new', 'POST', authorization_token, params=None, body=body)
