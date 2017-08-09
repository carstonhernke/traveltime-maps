import requests, json, numpy as np

def generate_times_matrix(coordinates):
    #coordinates = np.genfromtxt("coordinates.csv", delimiter=",")
    loc_str = str("")
    for i in range(0, coordinates.shape[0]):
        loc_str = loc_str+str(coordinates[i,2])+","+str(coordinates[i,1])+";"
    loc_str = loc_str[:-1]
    payload = ""
    link = "http://127.0.0.1:5000/table/v1/driving/"+str(loc_str)
    r = requests.get(link, params=payload)
    rj = json.loads(r.text)
    #print(rj)
    data = np.zeros((coordinates.shape[0],coordinates.shape[0]))
    k = 0
    for i in range(0, coordinates.shape[0]):
        for j in range(0, coordinates.shape[0]):
            data[i, j] = rj['durations'][i][j]
            #print(k)
            k += 1
    print(data)
    #np.savetxt(fname = "times_mpls_bike.csv", X = data, delimiter =',')
    return data
