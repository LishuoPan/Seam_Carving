'''
  File name: cumMinEngHor.py
  Author:
  Date created:
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the horizontal seam directions.
    
    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT My: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - OUTPUT Tby: n × m matrix representing the backtrack table along horizontal direction.
'''
import numpy as np

def cumMinEngHor(e):
  # Your Code Here
  # shape of energy matrix
  n, m = e.shape
  # initialize the My and Tby matrix
  My = np.zeros((n, m))
  My[:, 0] = e[:, 0]
  Tby = np.zeros((n, m), dtype=int)
  # DP to complete My and Tby
  k = 1
  # start from the second row
  for j in range(1, m):
    for i in range(n):
      predecessor_list = []
      predecessor_indx = []
      for ki in range(-k, k+1):
        if i + ki < 0 or i + ki > n-1:
          continue
        else:
          # predecessor_list.append(My[i-1, j+ki])
          predecessor_list.append(My[i+ki, j-1])
          predecessor_indx.append(ki)
      V_min_indx = np.argmin(predecessor_list)
      V_min = predecessor_list[V_min_indx] + e[i, j]
      Tb_element = predecessor_indx[V_min_indx]
      My[i, j] = V_min
      Tby[i, j] = Tb_element
  # print()
  return My, Tby


