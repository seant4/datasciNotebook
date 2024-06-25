import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

x = plt.imread('cat.jpg').astype(np.uint8)

R = x[:,:,0]
G = x[:,:,1]
B = x[:,:,2]

UR, SR, VR = np.linalg.svd(R)
UG, SG, VG = np.linalg.svd(G)
UB, SB, VB = np.linalg.svd(B)

r = 25
SR_d = np.diag(SR)
R = UR[:, :r] @ SR_d[:r, :r] @ VR[:r, :]
SG_d = np.diag(SG)
G = UG[:, :r] @ SG_d[:r, :r] @ VG[:r, :]
SB_d = np.diag(SB)
B = UB[:, :r] @ SB_d[:r, :r] @ VB[:r, :]

R = np.clip(R, 0, 255).astype(np.uint8)
G = np.clip(G, 0, 255).astype(np.uint8)
B = np.clip(B, 0, 255).astype(np.uint8)

compressed = np.dstack((R, G, B))
img.imsave('compressed.jpg', compressed)
