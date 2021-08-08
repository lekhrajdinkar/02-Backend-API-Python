from rest_framework.views import APIView
from rest_framework.response import Response
from pytz import all_timezones, country_names
from timezone_api import serializer
from rest_framework import status

class TimezomeAPI(APIView):
    """
    REST api to get timezones, datetime, date, time and country code using pytz module
    json : {"name":"lekhraj", "code":"123"}
    """

    tzserializer = serializer.TzSerializer

    def get(self, request, format=None):
        """get all timezones"""
        country_codes = self.getAllCountryName()
        return Response({
            'desc':'list of harcoded Country codes',
            'codes': country_codes,
            'all-timezones': all_timezones,
        })

    def post(self,request):
        """ json : {"name":"lekhraj", "code":"123"}"""

        s = self.tzserializer(data=request.data)
        if s.is_valid():
            name = s.validated_data.get('name')
            return Response({'message': f'hello {name}'
                             })
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


    # =============== Util ==================

    def getAllCountryName(self) -> list:
        result = list()
        for code in country_names:
            result.append(f'{code} : {country_names[code]}')
        return result