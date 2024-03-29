import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_rent(location,total_sqft,bhk,furnish):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bhk
    x[2] = furnish
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],0)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are total_sqft,bhk,furnish

    global __model
    if __model is None:
        with open('./artifacts/Hyderabd_house_rent_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_rent('Puppalaguda',2000, 3, 2))
    print(get_estimated_rent('Ameerpet, NH', 1000, 2, 1))
