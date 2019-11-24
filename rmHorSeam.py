'''
  File name: rmHorSeam.py
  Author:
  Date created:
'''

'''
  File clarification:
    Removes horizontal seams. You should identify the pixel from My from which 
    you should begin backtracking in order to identify pixels for removal, and 
    remove those pixels from the input image. 
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT My: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - INPUT Tby: n × m matrix representing the backtrack table along horizontal direction.
    - OUTPUT Iy: (n − 1) × m × 3 matrix representing the image with the row removed.
    - OUTPUT E: the cost of seam removal.
'''
import numpy as np
from helper import *


def rmHorSeam(I, My, Tby):
  # Your Code Here
  n, m = My.shape
  last_col = My[:, -1]
  lowest_energy_index = np.argmin(last_col)
  # find the removal cost
  E = last_col[lowest_energy_index]
  # recursively find the shortest path
  start_point = (lowest_energy_index, m-1)
  path = shortest_path_hor(start_point, Tby)
  # print(path)
  flat_path = list(map(lambda x: x[0] + x[1] * n, path))
  # print(flat_path)
  # print(len(flat_path))
  # delete the path in vector manner
  flat_I0 = I[:, :, 0].flatten('F')
  flat_I1 = I[:, :, 1].flatten('F')
  flat_I2 = I[:, :, 2].flatten('F')

  reduce_flat_I0 = np.delete(flat_I0, flat_path)
  reduce_flat_I1 = np.delete(flat_I1, flat_path)
  reduce_flat_I2 = np.delete(flat_I2, flat_path)

  # reform the array into (n,m-1)
  reformed_I0 = reduce_flat_I0.reshape(n - 1, m, order='F')
  reformed_I1 = reduce_flat_I1.reshape(n - 1, m, order='F')
  reformed_I2 = reduce_flat_I2.reshape(n - 1, m, order='F')
  # construct the Ix matrix
  Iy = np.zeros((n - 1, m, 3))
  Iy[:, :, 0] = reformed_I0
  Iy[:, :, 1] = reformed_I1
  Iy[:, :, 2] = reformed_I2
  return Iy, E

