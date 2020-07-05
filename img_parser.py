import base64
from PIL import Image
import numpy as np
import io

def base64_to_array(base64_string):
    '''
    output array shape: (width, height, 4)
    '''
    image = base64.b64decode(base64_string)  

    img = Image.open(io.BytesIO(image))

    return np.array(img)

def base64_to_y_values(base64_string):
    '''
    y_values = [np.nan, np.nan, -10, -8, -6, ... , 8, 10, np.nan]
    '''
    img_array = base64_to_array(base64_string)

    width, height, _ = img_array.shape
    array_2d = np.max(img_array, axis=2)
    y_indices = np.argmax(array_2d, axis=0)

    return [int(height / 2) - index if index else np.nan for index in y_indices]

def array_to_base64(numpy_array):
    '''
    intput array shape: (width, height, 4)
    '''

    in_mem_file = io.BytesIO()
    img = Image.fromarray(numpy_array)
    
    img.save(in_mem_file, format = "PNG")
    in_mem_file.seek(0)
    img_bytes = in_mem_file.read()

    base64_encoded_result_bytes = base64.b64encode(img_bytes)
    base64_encoded_result_str = base64_encoded_result_bytes.decode('ascii')

    return base64_encoded_result_str

def y_values_to_base64(y_values):
    '''
    y_values = [np.nan, np.nan, -10, -8, -6, ... , 8, 10, np.nan]
    '''
    len_y_values = len(y_values)
    y_indices = [int(len_y_values / 2) - value if value else value for value in y_values]
    coordinates = [(y_indices[i], i, 3) for i in range(len_y_values) if not np.isnan(y_indices[i])]

    return_array = np.zeros((len_y_values, len_y_values, 4), dtype="uint8")
    for coordinate in coordinates:
        return_array[coordinate] = 255

    return array_to_base64(return_array)
