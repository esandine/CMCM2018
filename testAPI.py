import json
import urllib2
import numpy as np

f = open("key.txt", "r")
key = f.read().strip()
f.close()

def buildurl(long_1,lat_1,long_2,lat_2):
    long_1=str(long_1)
    lat_1=str(lat_1)
    long_2=str(long_2)
    lat_2=str(lat_2)
    return "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+long_1+","+lat_1+"&destinations="+long_2+","+lat_2+"&key="+key

def read_json(url):
    return json.loads(urllib2.urlopen(url).read())

def gettime(long_1,lat_1,long_2,lat_2):
    url=buildurl(long_1,lat_1,long_2,lat_2)
    j = read_json(url)

    if 'status_code' in j:
        if j['status_code'] == 7:
            return "Whoops! The API key didn't work."
    elif 'total_results' in j and j['total_results'] > 0:
        return titles(get_ids(j))

    return j['rows'][0]['elements'][0]['duration']['value']
       
#print gettime(42.443164, -76.494008,42.436991, -76.510420)

#creates a list of n*m points that fill up the rectangle with upper left and lower right given by the coordinates, with m dots in the latitude direction, and n dots in the longitude direction
def listpoints(lat_1,long_1,lat_2,long_2,m,n):
    l=[]
    for i in range(1,m+1):
        for j in range(1,n+1):
            i=i*1.0
            j=j*1.0
            l.append(((1-(i-1)/(m-1))*lat_1+(i-1)/(m-1)*lat_2,(1-(j-1)/(n-1))*long_1+(j-1)/(n-1)*long_2))
    return l

def gentimematrix(lcoors):
    n=len(lcoors)
    timetable=np.zeros((n,n),int)
    for i in range(0,n):
        for j in range(0,n):
            if i<j:
                timetable[i][j]=gettime(lcoors[i][0],lcoors[i][1],lcoors[j][0],lcoors[j][1])
    return timetable

def saveMatrix(M,filename):
    retstr=""
    i=0
    j=0
    while i<len(M):
        while j< len(M[i]):
            retstr+=str(M[i][j])
            retstr+=" "
            j=j+1
        retstr=retstr[:-1]
        retstr+='; '
        j=0
        i=i+1
    retstr=retstr[:-2]
    f=open(filename,"w")
    f.write(retstr)
    f.close()

def readMatrix(filename):
    f=open(filename,"r")
    input=f.read()
    f.close()
    aSplit = input.split('; ')
    l = []
    for item in aSplit:
        subl = []
        for num in item.split(' '):
            subl.append(float(num))
        l.append(subl)
            
    return np.array(l)

A=listpoints(42.448953, -76.510167,42.442882, -76.494302,2,3)
A = gentimematrix(A)
saveMatrix(A,"twobythree.txt")
print np.array2string(readMatrix("twobythree.txt"))
