from carv import carv
import numpy as np
from PIL import Image

if __name__ == '__main__':
    # main script
    seams_removal = 20
    source_file_name = 'source.jpg'
    I = np.array(Image.open(source_file_name).convert('RGB'))
    # seam removal and gif creation will happen in the carv function
    carv(I, seams_removal, seams_removal)
