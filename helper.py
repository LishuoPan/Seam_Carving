import imageio
import numpy as np

def shortest_path_ver(start_point, Tbx):
  # initialization
  path = []
  path.append(start_point)
  direction = Tbx[start_point]
  n, m = Tbx.shape
  current_col_indx = start_point[1]
  # start link up to the top
  for i in range(1, n):
    # update the (row,col) coor
    current_row_indx = n-1-i
    current_col_indx = current_col_indx + direction
    # record coor
    current_coor = (current_row_indx, current_col_indx)
    # append the new coor to the path
    path.append(current_coor)
    # update the direction
    direction = Tbx[current_coor]
  return path

def shortest_path_hor(start_point, Tby):
  # initialization
  path = []
  path.append(start_point)
  direction = Tby[start_point]
  n, m = Tby.shape
  current_row_indx = start_point[0]
  # start link up to the top
  for j in range(1, m):
    # update the (row,col) coor
    current_col_indx = m-1-j
    current_row_indx = current_row_indx + direction
    # record coor
    current_coor = (current_row_indx, current_col_indx)
    # append the new coor to the path
    path.append(current_coor)
    # update the direction
    direction = Tby[current_coor]
  return path

def shortest_path_delete_imags(image_map, Tbt):
  n, m = Tbt.shape
  path = []
  imgs = []
  current_coor = (n-1, m-1)  # (nr,nc)
  imgs.append(image_map[current_coor])
  # compute the shortest path's length
  path_len = current_coor[0]+current_coor[1]
  direction = Tbt[current_coor]
  path.append(direction)
  for i in range(path_len):
    # 1 is left and 2 is up
    if direction == 1:
      current_coor = (current_coor[0], current_coor[1]-1)
    elif direction == 2:
      current_coor = (current_coor[0]-1, current_coor[1])
    imgs.append(image_map[current_coor])
    direction = Tbt[current_coor]
    path.append(direction)
  # reverse two list to start from top
  path = list(reversed(path))
  path_imgs = list(reversed(imgs))
  # print()
  return path, path_imgs


def make_gif(N, M, path_imags):
  # pad the image
  for indx, img in enumerate(path_imags):
    pad_img = np.zeros((N, M, 3))
    n, m, _ = img.shape
    pad_img[:, :, 0] = np.pad(img[:, :, 0], ((0, N - n), (0, M - m)), 'constant')
    pad_img[:, :, 1] = np.pad(img[:, :, 1], ((0, N - n), (0, M - m)), 'constant')
    pad_img[:, :, 2] = np.pad(img[:, :, 2], ((0, N - n), (0, M - m)), 'constant')
    path_imags[indx] = pad_img

  images_set = np.zeros((len(path_imags), N, M, 3))
  for i in range(len(path_imags)):
    images_set[i, :, :, :] = path_imags[i].astype(np.uint8)
  exportname = "output.gif"
  imageio.mimsave(exportname, images_set, 'GIF', duration=0.1)

