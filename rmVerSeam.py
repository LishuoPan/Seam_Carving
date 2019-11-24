'''
  File name: rmVerSeam.py
  Author:
  Date created:
'''

'''
  File clarification:
    Removes vertical seams. You should identify the pixel from My from which 
    you should begin backtracking in order to identify pixels for removal, and 
    remove those pixels from the input image. 
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT Mx: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - INPUT Tbx: n × m matrix representing the backtrack table along vertical direction.
    - OUTPUT Ix: n × (m - 1) × 3 matrix representing the image with the row removed.
    - OUTPUT E: the cost of seam removal.
'''
import numpy as np
from helper import *


def rmVerSeam(I, Mx, Tbx):
  # Your Code Here
  n, m = Mx.shape
  last_row = Mx[-1, :]
  lowest_energy_index = np.argmin(last_row)
  # find the removal cost
  E = last_row[lowest_energy_index]
  # recursively find the shortest path
  start_point = (n-1, lowest_energy_index)
  path = shortest_path_ver(start_point, Tbx)
  # print(path)
  flat_path = list(map(lambda x: x[0]*m + x[1], path))
  # print(flat_path)
  # print(len(flat_path))
  # delete the path in vector manner
  flat_I0 = I[:, :, 0].flatten()
  flat_I1 = I[:, :, 1].flatten()
  flat_I2 = I[:, :, 2].flatten()

  reduce_flat_I0 = np.delete(flat_I0, flat_path)
  reduce_flat_I1 = np.delete(flat_I1, flat_path)
  reduce_flat_I2 = np.delete(flat_I2, flat_path)

  # reform the array into (n,m-1)
  reformed_I0 = reduce_flat_I0.reshape(n, m-1)
  reformed_I1 = reduce_flat_I1.reshape(n, m-1)
  reformed_I2 = reduce_flat_I2.reshape(n, m-1)
  # construct the Ix matrix
  Ix = np.zeros((n, m-1, 3))
  Ix[:, :, 0] = reformed_I0
  Ix[:, :, 1] = reformed_I1
  Ix[:, :, 2] = reformed_I2
  return Ix, E


