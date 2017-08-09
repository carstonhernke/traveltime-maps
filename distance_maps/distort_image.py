import cv2
from scipy.interpolate import griddata
import numpy as np
#from sklearn import preprocessing

def start_grid(xdim,ydim,xmax,ymax):
    k = 0
    mat = np.zeros((xdim*ydim,2))
    for i in range(0, xdim):
        for j in range(0, ydim):
            mat[k,0] = int(i*(xmax/xdim))
            mat[k,1] = int(j*(ymax/ydim))
            k += 1
    return mat

def rescale(in_mat,new_range):
    out_mat = np.ones_like(in_mat)
    for i in range(0,2):
        max_ = max(in_mat[:,i])
        min_ = min(in_mat[:,i])
        in_range = max_ - min_
        out_range = new_range
        for j in range(0,in_mat.shape[0]):
            out_mat[j,i] = int((((in_mat[j,i]-min_)*out_range)/in_range) + 0)
    return out_mat

def distort_image(fitted_coordinates, map_to_distort)
    grid_xy = start_grid(1000,1000,1000,1000)
    raw_output = np.genfromtxt("/Users/carstonhernke/PycharmProjects/geodata/fitted_coordinates_mpls.csv", delimiter=",")
    raw_output = np.delete(raw_output, (0), axis = 0)
    output_trim = raw_output[:,[1,2]]
    output_coordinates = rescale(output_trim,1000)
    input_coordinates = start_grid(10,10,1000,1000)

    grid_z = griddata(input_coordinates, output_coordinates, grid_xy, method='cubic')

    map_x = grid_z[:,0]
    map_y = grid_z[:,1]
    map_x = np.reshape(map_x,(1000,1000))
    map_y = np.reshape(map_y,(1000,1000))
    map_x_f32 = np.flipud(map_x).astype('float32')
    map_y_f32 = np.flipud(map_y).astype('float32')

    orig_map = cv2.imread(map_to_distort)
    distorted = cv2.remap(orig_map, map_x_f32, map_y_f32, interpolation = cv2.INTER_CUBIC)
    cv2.imwrite("distorted_map.png", distorted)
    return 0