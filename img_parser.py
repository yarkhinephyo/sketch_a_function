import base64
from PIL import Image
import numpy as np
import io

def to_array(base64_string):
    image = base64.b64decode(base64_string)       

    img = Image.open(io.BytesIO(image))

    return np.array(img)

def to_base64(numpy_array):
    in_mem_file = io.BytesIO()
    img = Image.fromarray(numpy_array)
    
    img.save(in_mem_file, format = "PNG")
    in_mem_file.seek(0)
    img_bytes = in_mem_file.read()

    base64_encoded_result_bytes = base64.b64encode(img_bytes)
    base64_encoded_result_str = base64_encoded_result_bytes.decode('ascii')

    return base64_encoded_result_str