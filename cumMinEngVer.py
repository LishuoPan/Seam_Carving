'''
  File name: cumMinEngVer.py
  Author:
  Date created:
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the vertical seam directions.
    
    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT Mx: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - OUTPUT Tbx: n × m matrix representing the backtrack table along vertical direction.
'''
import numpy as np

def cumMinEngVer(e):
  # Your Code Here
  # shape of energy matrix
  n, m = e.shape
  # initialize the My and Tby matrix
  Mx = np.zeros((n, m))
  Mx[0, :] = e[0, :]
  Tbx = np.zeros((n, m), dtype=int)
  # DP to complete My and Tby
  k = 1
  # start from the second row
  for i in range(1, n):
    for j in range(m):
      predecessor_list = []
      predecessor_indx = []
      for ki in range(-k, k + 1):
        if j + ki < 0 or j + ki > m - 1:
          continue
        else:
          predecessor_list.append(Mx[i - 1, j + ki])
          predecessor_indx.append(ki)
      V_min_indx = np.argmin(predecessor_list)
      V_min = predecessor_list[V_min_indx] + e[i, j]
      Tb_element = predecessor_indx[V_min_indx]
      Mx[i, j] = V_min
      Tbx[i, j] = Tb_element
  # print()
  return Mx, Tbx


