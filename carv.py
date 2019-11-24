'''
  File name: carv.py
  Author:
  Date created:
'''

'''
  File clarification:
    Aimed to handle finding seams of minimum energy, and seam removal, the algorithm
    shall tackle resizing images when it may be required to remove more than one seam, 
    sequentially and potentially along different directions.
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT nr: the numbers of rows to be removed from the image.
    - INPUT nc: the numbers of columns to be removed from the image.
    - OUTPUT Ic: (n − nr) × (m − nc) × 3 matrix representing the carved image.
    - OUTPUT T: (nr + 1) × (nc + 1) matrix representing the transport map.
'''
import numpy as np
from cumMinEngVer import cumMinEngVer
from cumMinEngHor import cumMinEngHor
from rmVerSeam import rmVerSeam
from rmHorSeam import rmHorSeam
from genEngMap import genEngMap
from helper import *



def carv(I, nr, nc):
  # Your Code Here
  N, M, _ = I.shape
  # construct the empty matrix T
  T = np.zeros((nr + 1, nc + 1))
  # initialize the mapping dictionary
  image_map = {}
  image_map[(0, 0)] = I
  # initial the track table, 1 is left and 2 is up
  Tbt = np.zeros((nr + 1, nc + 1))
  Tbt[0, :] = 1
  Tbt[:, 0] = 2
  Tbt[0, 0] = 0

  # fill the first row and col of the T matrix
  for i in range(1, nr + 1):
    # new coor
    coor = (i, 0)
    up_coor = (i-1, 0)
    I_up = image_map[up_coor]
    # new image with one row deleted
    e = genEngMap(I_up)
    My, Tby = cumMinEngHor(e)
    Iy, E = rmHorSeam(I_up, My, Tby)
    # add the new image to the dict and fill the (i,0) of E matrix
    image_map[coor] = Iy
    T[coor] = T[up_coor] + E

  for j in range(1, nc + 1):
    # new coor
    coor = (0, j)
    left_coor = (0, j-1)
    I_left = image_map[left_coor]
    # new image with one column deleted
    e = genEngMap(I_left)
    Mx, Tbx = cumMinEngVer(e)
    Ix, E = rmVerSeam(I_left, Mx, Tbx)
    # add the new image to the dict and fill the (0,j) of E matrix
    image_map[coor] = Ix
    T[coor] = T[left_coor] + E


  # DP to complete T matrix
  for ii in range(1, nr + 1):
    for jj in range(1, nc + 1):
      coor = (ii, jj)
      up_coor = (ii - 1, jj)
      left_coor = (ii, jj - 1)

      candidate_img_list = []
      cost_list = []
      # grow from left, delete col
      I_left = image_map[left_coor]
      e = genEngMap(I_left)
      Mx, Tbx = cumMinEngVer(e)
      Ix, Ex = rmVerSeam(I_left, Mx, Tbx)
      # Ix = np.pad(Ix, ((0, ii), (0, jj)), 'constant')
      cost_from_left = Ex + T[left_coor]
      # grow from up, delete row
      I_up = image_map[up_coor]
      e = genEngMap(I_up)
      My, Tby = cumMinEngHor(e)
      Iy, Ey = rmHorSeam(I_up, My, Tby)
      # Iy = np.pad(Iy, ((0,ii),(0,jj)), 'constant')
      cost_from_up = Ey + T[up_coor]
      # construct cost list (2 elements)
      cost_list.append(cost_from_left)
      cost_list.append(cost_from_up)
      # add candidate imgs to the list
      candidate_img_list.append(Ix)
      candidate_img_list.append(Iy)
      # construct Tbt and T table
      # 1 is left and 2 is up
      indentify_direction = np.argmin(cost_list)
      Tbt[ii, jj] = indentify_direction + 1
      T[ii, jj] = cost_list[indentify_direction]
      image_map[coor] = candidate_img_list[indentify_direction]
  # from (nr,nc) trace back along the shortest path
  path, path_imags = shortest_path_delete_imags(image_map, Tbt)
  # for the return Ic image
  Ic = path_imags[-1]

  # make the gif
  make_gif(N, M, path_imags)

  return Ic, T


