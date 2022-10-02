import numpy as np
import cv2

def read_byte_img(byte_img):
    """Reading incoming bytearray image

    Parameters
    ----------
    byte_img : bytearray
        Incoming image

    Returns
    -------
    image : np.array
        Image in np array format
    """
    image = np.asarray(bytearray(byte_img), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def process_image(image):
    """Process read image, crop, rotate, etc.
    
    Parameters
    ----------
    image : np.array
        Image as an np.array
    
    Returns
    -------
    image : np.array
        Processed image in np.array format
    """
    return True

def draw_mask(image, coordinates, mask):
    """Draws mask on a given coordinates 
    
    Parameters
    ----------
    image : np.array
        Image as an np.array
    coordniates : list
        List of coordinates
    mask : int
        ID of a mask to draw
    
    Returns
    -------
    image : np.array
        Image with mask drawn on it in np.array format
    """
    return True

