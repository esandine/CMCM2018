import json
import urllib2

f = open("key.txt", "r")
key = f.read().strip()
f.close()

def buildurl(long_1,lat_1,long_2,lat_2):
    long_1=str(long_1)
    lat_1=str(lat_1)
    long_2=str(long_2)
    lat_2=str(lat_2)
    return "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+long_1+","+lat_1+"&destinations="+long_2+","+lat_2+"&key="+key

print buildurl(42.443164, -76.494008,42.436991, -76.510420)
