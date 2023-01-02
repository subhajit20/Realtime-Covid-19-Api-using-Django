from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import CountryNameSerializer
from channels.layers import channel_layers,get_channel_layer
# Create your views here.

# internal imports
from .lib.covid19 import GetCovid19RealtimeData

@api_view(["GET"])
def GetCovid19data(request):
    data = GetCovid19RealtimeData()
    try:
        if data is not None:
            return Response({
                "Status":200,
                "Flag":True,
                "Data":data
            })
        else:
            return Response({
                "Status":404,
                "Flag":False,
                "msg":"No Data Found..."
            })
    except Exception as e:
        return Response({
            "Status":500,
            "Flag":False,
            "error":"Something went wrong..."
        })

# layer = get_channel_layer()
@api_view(["POST"])
def SearchbyCountryName(request):
    try:
        serializer = CountryNameSerializer(data=request.data)
        if serializer.is_valid():
            data = GetCovid19RealtimeData()
            if len(data) > 0:
                searcheddata = [i for i in data if serializer.data["name"] == i["Country"]]
                print(searcheddata)
                if searcheddata is not None:
                    return Response({
                        "Status":200,
                        "Flag":True,
                        "Data":searcheddata
                    })
                else:
                     return Response({
                        "Status":404,
                        "Flag":False,
                        "msg":"No Country Found with this name..."
                    })
            else:
                return Response({
                    "Status":502,
                    "Flag":False,
                    "error":serializer.errors
                })
        else:
            return Response({
                        "Status":404,
                        "Flag":False,
                        "msg":"No Data Found..."
                    })
    except Exception as e:
        return Response({
            "Status":500,
            "Flag":False,
            "error":"Something went wrong..."
        })