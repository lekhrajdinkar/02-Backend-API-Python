from rest_framework.views import APIView
from rest_framework.response import Response
from pytz import all_timezones, country_names
from timezone_api import serializer
from rest_framework import status
from rest_framework import viewsets

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

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})

    # =============== Util ==================

    def getAllCountryName(self) -> list:
        result = list()
        for code in country_names:
            result.append(f'{code} : {country_names[code]}')
        return result

class TimezoneViewSet(viewsets.ViewSet):
    """ TEST  API """

    tzserializer = serializer.TzSerializer

    def list(self, request):
        return Response({'method': 'list', 'message': ['abc', 'efg']})

    def create(self, request):
        s = self.tzserializer(data=request.data)
        return Response({'method': 'post', 'desc': 'create object on server'})

    def retrieve(self, request, pk=None):
        return Response({'method': 'GET', 'desc': 'get object by id'})

    def update(self, request, pk=None):
        return Response({'method': 'PUT', 'desc': 'update object by id'})

    def partial_destroy(self, request, pk=None):
        return Response({'method': 'PUT', 'desc': 'updating part of object'})

    def destroy(self, request, pk=None):
        return Response({'method': 'DELETE', 'desc': 'delete object'})

    # def list(self, request):
    #     return Response({'method': 'list'})
    #
    # def list(self, request):
    #     return Response({'method': 'list'})
    #
    # def list(self, request):
    #     return Response({'method': 'list'})
