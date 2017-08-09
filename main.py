from matrix_import import generate_times_matrix
from distort_image import distort_image
from get_map import get_map
from generate_coordinates import generate_coordinates

### set parameters
map_center_point_lat = 44.9745
map_center_point_lon = -93.2676
zoom = 14
zoom_width_deg = .022 #find degree value corresponding to zoom level here: http://wiki.openstreetmap.org/wiki/Zoom_levels

coordinates = generate_coordinates(map_center_point_lat, map_center_point_lon, zoom_width_deg) #this generates a 100x100 matrix of coordinates based on your center point and zoom level
map_file = get_map(map_center_point_lat, map_center_point_lon, zoom, osm_token) #gets the requested map tiles from OSM, saves them locally, and stores the filename

# before you run this line you need to have an OSRM-backend running on your computer. See instructions here: https://hub.docker.com/r/osrm/osrm-backend/
# this will generate a 100x100 matrix representing the travel times between each of the coordinates

times_matrix = generate_times_matrix(coordinates)
p.savetxt(fname = "times_matrix.csv", X = times_matrix, delimiter =',') # saves the times matrix so it can be imported into R

# *Next you have to use R to run the PCoA algorithm - run the file "PCoA.R"*

fitted_coordinates = np.genfromtxt("fitted_coordinates.csv", delimiter=",") # reads the file that R exported

distort_image(fitted_coordinates,map_file) # distorts the map using cv2.remap and saves it as distorted_map.png


