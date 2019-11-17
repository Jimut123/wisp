"""
#   Copyright (c) 2019, Jimut Bahan Pal. All Rights Reserved.
#
#   Please refer to the GNU GENERAL PUBLIC LICENSE for more.
#
#   This is the application (probably simple) to find the location (almost any) in any Country 
#   according to the choices of your preference. Uses Foursquare API to get the data (geojson).
#   Please provide the Access key for the API, if bychance not given! This then creates a map to visualise the locations
#   in a web browser, because Folium (leaflet.js) doesn't work in GUI or Terminal.
#   
#   Caution: Please don't blame me if this doesn't works, cause the data may not be present for 
#            some location, since everyone will use free services of foursquare API.
#
#   e-mail : jimutbahanpal@yahoo.com
#   website : https://jimut123.github.io
#   Created for the purpose of final year project! :=> Almost data visualization project!
#   
#   Updated == version 2.0, uses JJ-Cluster custom made algorithm.
#   Dated : 17-11-2019
"""



from http.server import BaseHTTPRequestHandler, HTTPServer
from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values
import requests # library to handle requests
import pandas as pd # library for data analsysis
import numpy as np # library to handle data in a vectorized manner
import random # library for random number generation
# tranforming json file into a pandas dataframe library
from pandas.io.json import json_normalize
from IPython.core.display import HTML 
from IPython.display import Image 
from datetime import datetime
import webbrowser
import subprocess
import argparse
import folium # plotting library
import json

print('Folium installed')
print('Libraries imported.')

CLIENT_ID = '' # your Foursquare ID
CLIENT_SECRET = '' # your Foursquare Secret
VERSION = '20180604'
LIMIT = 30

def time_now():
    format = "1;32;40"
    s1 = ''
    time_stmp = datetime.now().isoformat(timespec='seconds')
    s1 += '\x1b[%sm %s \x1b[0m' % (format, time_stmp)
   
    print("running app : {} ".format(s1),end="")

# this reads the secrets from the secret.txt file and returns them in tuple format!
try:
    time_now()
    print("Fetching credentials from secrets.txt file")
    with open('secrets.txt', 'r') as f:
        array = json.load(f)
    print('Your credentails:')

    CLIENT_ID = str(array['client_id'])
    CLIENT_SECRET = str(array['client_secret'])
    time_now()
    print('CLIENT_ID: ' + CLIENT_ID)
    time_now()
    print('CLIENT_SECRET: ' + CLIENT_SECRET)
   
except:
    print("NO SECRETS PRESENT, please enter it in text file secrets.txt in future...\n ")
    print("create a file named as secrets.txt and put these contents ::=> ")
    print("""\
        {
            "client_id":"your client ID",
            "client_secret":"your client secret"
        }
        """)
            
address = input("ENTER ADDRESS : \n")
time_now()
radius = input("Enter radius :\n")
time_now()
geolocator = Nominatim(timeout=10)
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print(latitude, longitude)
data_ice = []
No_Q = input("Enter number of Queries : \n")
time_now()
import json




for i in range(int(No_Q)):
    print("{} ".format(i),end="")
    time_now()
    search_query = input("Enter Search Query : ")
    
    print(search_query + ' .... OK!')

    url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&v={}&query={}&radius={}&limit={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, search_query, radius, LIMIT)
    #url
    results = requests.get(url).json()
    item = results['response']['venues']
    #print(json.dumps(item, indent=4, sort_keys=True))
    for item_ in item:
        #print(json.dumps(item_, indent=4, sort_keys=True))
        name = item_["name"]
        cat = item_["categories"]
        loc = ', '.join(item_["location"]["formattedAddress"])
        lat_ = item_["location"]["lat"]
        lon_ = item_["location"]["lng"]
        #add = item_["location"]
        #print(name)
        #print(cat)
        #print(loc)
        #print(lat_,"   +   ",lon_)
        data_ice.append((search_query,"{}\n and Location : {}".format(name,loc),lat_,lon_))

    #print(data_ice)    
    print("DONE COMPLETED")
"""

Algorithm:
    
    Initialise vertex_list
    
    1. Find the minimum distance for class 1 and append it to vertex list.
    2. For every other class find min distance to vertex_list and add it to vertex_list
    3. find the minimum distance from addition of verteces to the list and add the next node to the list

"""




from math import sin, cos, sqrt, atan2, radians
import random # library for random number generation
import folium # plotting library

# approximate radius of earth in km
R = 6373.0

def ret_dist(lat1,lon1,lat2,lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    #print("Result:", distance)
    #print("Should be:", 278.546, "km")
    return distance
string_gen = "0123456789abcdef"
def get_random_col():
    # unnecessary stuffs to make the visualization cool
    ret_str = "#"
    for i in range(6):
        ret_str += random.choice(string_gen)
    return ret_str

def Jimut_Wisp_Cluster3_Minimum(map_data):
    time_now()
    print("Select the Map types [0/1/2/3/4] and then press Enter :: ")
    MAP_TYPES = ["Mapbox Bright","Stamen Toner","Stamen Terrain","OpenStreetMap","Mapbox Control Room"]
    name_type = int(input("\n 0 - Mapbox Bright\n 1 - Stamen Toner\n 2 - Stamen Terrain\n 3 - OpenStreetMap\n 4 - Mapbox Control Room ::=> \n"))
    MAP = folium.Map(location=[latitude, longitude],tiles=MAP_TYPES[name_type], zoom_start=11)

    name=map_data[0][0]
    LEGEND_DATA = []
    full_tree = []
    data_cate = []
    OVER_COL = str(get_random_col())
    FILL_COL = str(get_random_col())
    LEGEND_DATA.append([name,OVER_COL,FILL_COL])
    for item in map_data:
        lat = item[2]
        lng = item[3]
        #print(item," => ")
        if(item[0]!=name):
            OVER_COL = str(get_random_col())
            FILL_COL = str(get_random_col())
            full_tree.append([name,data_cate])
            name=item[0]
            LEGEND_DATA.append([name,OVER_COL,FILL_COL])
            data_cate=[]
            #print("got into first check")
        if(item[0]==name):
            data_cate.append([item[1],lat,lng])
            #print("got into 2nd check")
        label = "cat : {} \n, Name : {}".format(item[0],item[1])
        folium.CircleMarker(
                            [lat, lng],
                            radius=5,
                            popup=label,
                            color=OVER_COL,
                            fill=True,
                            fill_color=FILL_COL,
                            fill_opacity=0.7).add_to(MAP)
    full_tree.append([name,data_cate])
    min_dist_vert = []
    vert_only = []
    for i in full_tree:
        time_now()
        item_class = i[0]
        print(item_class)
        k_dummy=0
        print("i[1:][0] => ",i[1:][0])
        for item in i[1:][0]:
            # the upper class 
            name_point_ = item[0]
            name_lat_ = item[1]
            name_lon_ = item[2]

            final_dist=0
            print("item loop => ",name_point_," == ",name_lat_," == ",name_lon_)
            #
            for k in full_tree:
                # the sub class
                item_class2 = k[0]
                #print("class 2 => ",item_class2)
                if len(min_dist_vert) == 0:
                    if item_class2!=item_class:
                        #print("class 2 ",k)
                        for j in k[1:][0]:
                            name_point = j[0]
                            name_lat = j[1]
                            name_lon = j[2]
                            print(name_point," == ",name_lat," == ",name_lon,end="")
                            dist_from_item = ret_dist(name_lat_,name_lon_,name_lat,name_lon)
                            print(" dist from ",name_point_," to ",name_point," is:=> ",dist_from_item)
                            final_dist += dist_from_item
            if len(min_dist_vert)>0:

                if item_class2 not in vert_only:
                    print("class2 => ",item_class2)
                    print("\n\nmin_dist_vert => ",min_dist_vert)
                    for j in min_dist_vert:
                        name_point = j[0]
                        name_lat = j[1][0]
                        name_lon = j[1][1]
                        print("2nd check => ",name_point," == ",name_lat," == ",name_lon,end="")
                        dist_from_item = ret_dist(name_lat_,name_lon_,name_lat,name_lon)
                        print("[+] dist from ",name_point_," to ",name_point," is:=> ",dist_from_item)
                        final_dist += dist_from_item
            print("Total dist of ",name_point_," is => ",final_dist)

            if k_dummy==1:
                if minimum_dist>=final_dist:
                    minimum_dist = final_dist
                    min_dist_lat = name_lat_
                    min_dist_lon = name_lon_
                    min_dist_name = name_point_
                    print("Minimum => ",min_dist_name,"dist => ",minimum_dist," + ",min_dist_lat," + ",min_dist_lon)
            if k_dummy==0:
                minimum_dist=final_dist
                minimum_dist = final_dist
                min_dist_lat = name_lat_
                min_dist_lon = name_lon_
                min_dist_name = name_point_
                k_dummy=1
                print("dummy set to 1")
            print("$$$$Minimum => ",min_dist_name,"dist => ",minimum_dist," + ",min_dist_lat," + ",min_dist_lon)
        vert_only.append(item_class)
        min_dist_vert.append([min_dist_name,[min_dist_lat,min_dist_lon]])
        print("MIN DIST VERT LIST => ",min_dist_vert)
        
    for i1 in min_dist_vert:
        for j1 in min_dist_vert:
            p1 = i1[1]
            p2 = j1[1]
            print(p1,",",p2)
            folium.PolyLine(locations=[p1, p2], color='red',weight=1.5,opacity=1).add_to(MAP)
    #print(LEGEND_DATA)
    DOTS_HTML = ""
    for item in LEGEND_DATA:
        name_leg = item[0]
        over_leg = item[1]
        fill_leg = item[2]
        DOTS_HTML +="""
            &nbsp; {} &nbsp;
            <svg height="10" width="10">
            <circle cx="5" cy="5" r="4" stroke="{}" stroke-width="3" fill="{}" />
            </svg><br/> """.format(str(name_leg),str(over_leg),str(fill_leg))
    LEGEND_HTML = """
    <center>
    <h1 ><i style="color:#c6ae0d; font face=Arial,Helvetica "> WISP v2.0 </i></h1> 
    </center>
    
    <div id="legend-html" style="position: fixed; background-color: white; 
    bottom: 50px; left: 50px;  
    border:2px solid grey; z-index:9999; font-size:14px;" >&nbsp; 
    <b>Legend <b>
    <br>{}
    </div>
    <div style="position: fixed; 
    bottom: 50px; right: 50px;  
    z-index:9999; font-size:10px;
    "> 
    <b style="color:#f90404" style="align: justified">
        WISP <br/> 
        version: 2.0 <br/>
        &copyJimut Bahan Pal <br/> 
        Author : jimutbahanpal@yahoo.com 
    </b>
    </div>
    <div style="position: fixed; 
    top: 70px; left: 50px;  
    z-index:9999; font-size:15px;
    "> 
    <b style="color:#16842c" style="align: justified">
        Location: {} <br/>
        Lat, Lon: {},{} <br/>
        Radius: {} <br/>
        Date: {} <br/>
    </b>
    </div> 
    """.format(str(DOTS_HTML),address,latitude,longitude,radius,datetime.now().isoformat(timespec='seconds'))
    MAP.get_root().html.add_child(folium.Element(LEGEND_HTML))
    
    return MAP


if __name__ == "__main__":
    time_now()
    MAP = Jimut_Wisp_Cluster3_Minimum(data_ice)
    time_now()
    print("Saving file as ==> ","{}_{}.html".format(address,No_Q))
    MAP.save("{}_{}.html".format(address,No_Q))
    


