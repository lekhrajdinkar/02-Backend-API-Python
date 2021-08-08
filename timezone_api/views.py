from rest_framework.views import APIView
from rest_framework.response import Response
from pytz import all_timezones

class TimezomeAPI(APIView):
    """REST api to get timezones, datetime, date, time and country code using pytz module"""

    def get(self, request, format=None):
        """get all timezones"""
        country_codes = ['IN', 'TW', 'JP']
        return Response({
            'desc':'list of harcoded Country codes',
            'codes': country_codes,
            'all-timezones': all_timezones
        })
