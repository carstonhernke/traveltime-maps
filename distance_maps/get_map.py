#use the mapbox API to download and save a png map
import requests
import shutil

def get_map(lat_center,lon_center,zoom, osm_token):
    style = "streets-v10"
    lon_center = -93.2676
    lat_center = 44.9745
    zoom = 14
    bearing = 0
    pitch = 0
    size = "1000x1000"
    url = "https://api.mapbox.com/styles/v1/mapbox/"+str(style)+"/static/"+str(lon_center)+","+str(lat_center)+","+str(zoom)+","+str(bearing)+","+str(pitch)+"/"+size+"?access_token="+str(osm_token)+".png"
    #print(url)
    r = requests.get(url, stream = True)
    #print(r)
    file = 'map.png'
    with open(file, 'wb') as out_file:
        shutil.copyfileobj(r.raw, out_file)
    del r
    return file
