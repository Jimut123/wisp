from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E, N, S
# tranforming json file into a pandas dataframe library
from http.server import BaseHTTPRequestHandler, HTTPServer
from math import sin, cos, sqrt, atan2, radians
from pandas.io.json import json_normalize
from folium.plugins import MarkerCluster
from tempfile import NamedTemporaryFile
from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values
from IPython.core.display import HTML 
from IPython.display import Image
from datetime import datetime
from tkinter import *
import tkinter as tk
import pandas as pd # library for data analsysis
import numpy as np # library to handle data in a vectorized manner
import subprocess
import webbrowser
import requests # library to handle requests
import argparse
import random # library for random number generation
import folium # plotting library
import json
import os


def Jimut_cluster(map_data):
    import folium # plotting library
    """
    Takes in :=>
    map_data = [("Meat","Khasi",22.569098,88.366418),
            ("Meat","Chasi",22.562298,88.376218),
            ("Tea","My Tea",22.582298,88.367218),
            ("Museum","museum1",22.570298,88.352218),
            ("Museum","museum2",22.492298,88.362218),
            ("Museum","museum3",22.592298,88.307218),
            ("Chinese Res","Indo China",22.542298,88.397218),
            ("Thai Res","My Thai",22.535298,88.397218),
            ("Thai Res","Thaism",22.535298,88.387218),
            ("Thai Res","Nilu Thai",22.538298,88.396218),
            ("Airport","NSCB",22.338298,88.333218),
            ("Fishery","DODO Fishery",22.738298,88.696218),
            ("Motel","Baloo's Dhaba",22.608298,88.437218)
           ]
    Outputs=> Map
    """

    
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

    latitude =  22.569098
    longitude = 88.366418

    MAP = folium.Map(location=[latitude, longitude],tiles="Stamen Toner", zoom_start=11)

    name=map_data[0][0]

    full_tree = []
    data_cate = []
    OVER_COL = str(get_random_col())
    FILL_COL = str(get_random_col())
    for item in map_data:
        lat = item[2]
        lng = item[3]
        #print(item," => ")
        if(item[0]!=name):
            OVER_COL = str(get_random_col())
            FILL_COL = str(get_random_col())
            full_tree.append([name,data_cate])
            name=item[0]
            data_cate=[]
            #print("got into first check")
        if(item[0]==name):
            data_cate.append([item[1],lat,lng])
            #print("got into 2nd check")
        label = "cat : {}, Name : {}".format(item[0],item[1])
        folium.CircleMarker(
                            [lat, lng],
                            radius=5,
                            popup=label,
                            color=OVER_COL,
                            fill=True,
                            fill_color=FILL_COL,
                            fill_opacity=0.7).add_to(MAP)
    full_tree.append((name,data_cate))
    #MAP
    import pandas as pd 

    distance_api = []
    # for i in map_data:
    #     print(i[0],end=" ")
    # print()
    index_mat = []
    for i in map_data:
        lis = []
        index_mat.append(str(i[0]+"_"+i[1]))
        for j in map_data:

            #print(i[2],i[3]," ",j[2],j[3],end="")
            #distance_api.append([[i[2],i[3]],[j[2],j[3]],[ret_dist(i[2],i[3],j[2],j[3])]])
            lis.append(ret_dist(i[2],i[3],j[2],j[3]))
            #distance_api[([i[2],i[3])][([j[2],j[3]])] = ret_dist(i[2],i[3],j[2],j[3])
            #distance_api[i[1]][j[1]] = ret_dist(i[2],i[3],j[2],j[3])
            p1=[i[2],i[3]]
            p2=[j[2],j[3]]
            #print(DataFrame(ret_dist(i[2],i[3],j[2],j[3]),end="  "))
            folium.PolyLine(locations=[p1, p2], color='blue',weight=0.5,opacity=1).add_to(MAP)
        distance_api.append(lis)
        #print()
    #print(distance_api)
    #MAP
    list_dist_final = []

    for item in full_tree:
        add_dist = 0
        #print(item[0])
        for k in item[1:]:
            for var in k:
                name_ =  var[0]
                lat_ = var[1]
                lon_ = var[2]
                #print("POI => ",name_," ",lat_," ",lon_)
                # sub

                for item_ in full_tree:
                    if(item_[0]!=item[0]):
                        for k_ in item_[1:]:
                            for var_ in k_:
                                name__ =  var_[0]
                                lat__ = var_[1]
                                lon__ = var_[2]
                                #print(name__," ",lat__," ",lon__,end="")
                                dis = ret_dist(lat_,lon_,lat__,lon__)
                                #print(" dist => ",dis)
                                add_dist += dis
                #print("ADD DIST =====> ",add_dist)
                list_dist_final.append([item[0],name_,add_dist,[lat_,lon_]])
        
    #print(list_dist_final)
    # getting unique categories
    name_it = list_dist_final[0][0]
    min_ = list_dist_final[0][2]


    fin_opt_list = []
    for item in list_dist_final:
        if(name_it==item[0]):
            if(min_>=item[2]):
                cat_op = item[0]
                min_ = item[2]
                op_name = item[1]
                lat_lon = item[3:]
        if(name_it!=item[0]):
            fin_opt_list.append([cat_op,min_,op_name,lat_lon])
            min_ = item[2]
            name_it = item[0]
            cat_op = item[0]
            op_name = item[1]
            lat_lon = item[3:]
    fin_opt_list.append([cat_op,min_,op_name,lat_lon])
    #print(fin_opt_list)
    import pandas as pd 

    latitude =  22.569098
    longitude = 88.366418

    F_MAP = folium.Map(location=[latitude, longitude],tiles="Stamen Toner", zoom_start=11)
    for i in fin_opt_list:
        for j in fin_opt_list:
            p1 = i[3]
            p2 = j[3]
            #print(p1[0])
            #print(p2[0])
            folium.PolyLine(locations=[p1[0], p2[0]], color='red',weight=1.5,opacity=1).add_to(F_MAP)
    #F_MAP
    name=map_data[0][0]
    for item in map_data:
        lat = item[2]
        lng = item[3]
        #print(item," => ")
        if(item[0]!=name):
            OVER_COL = str(get_random_col())
            FILL_COL = str(get_random_col())
            name = item[0]
        label = "cat : {}, Name : {}".format(item[0],item[1])
        folium.CircleMarker(
                            [lat, lng],
                            radius=5,
                            popup=label,
                            color=OVER_COL,
                            fill=True,
                            fill_color=FILL_COL,
                            fill_opacity=0.7).add_to(F_MAP)
    print("DONE!")
    return F_MAP