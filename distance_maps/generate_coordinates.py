import math
import numpy

class Coord:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
def generate_coordinates(map_center_point_lat, map_center_point_lon, zoom_width_deg):
    map_center_point = Coord(44.9745,-93.2676)
    zoom_width_deg = .022 #find degree value corresponding to zoom level here: http://wiki.openstreetmap.org/wiki/Zoom_levels
    starting_point = Coord(map_center_point.lat-(zoom_width_deg/2), map_center_point.lon-(zoom_width_deg/2))  # this is the point in the SE (lower right) corner
    num_ptns = 10

    x_bound = 111111*math.cos(map_center_point.lat)*zoom_width_deg  # distance to cover in E/W direction (meters)
    y_bound = 111111*zoom_width_deg  # distance to cover in N/S direction (meters)
    resx = num_ptns/ x_bound # number of coordinates per axis
    resy = num_ptns/ y_bound

    ix = num_ptns
    jy = num_ptns
    data = numpy.zeros(((ix*jy), 3))
    k = 0
    for i in range(0, ix):
        for j in range(0, jy):
            new_lat = starting_point.lat + j*resy  # find new latitude based on moving north
            new_lon = starting_point.lon - i*resx  # not sure if the new or old lat should be used?
            data[k, 1] = new_lat
            data[k, 2] = new_lon
            data[k, 0] = k
            k += 1
            print(k)
    #numpy.savetxt(fname="coordinates_mpls.csv", X=data, delimiter=',')
    return data