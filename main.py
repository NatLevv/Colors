import cv2
import numpy as np

i = cv2.imread('image/color_text.jpg')    # Загрузка карт.

bi = np.zeros_like(i)    # черн.фон

gi = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)     # перевод в серый

coni = cv2.Canny(gi, 25, 50)   # поиск контуров карт.

con, hir = cv2.findContours(coni, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)    # поиск конт.текста

con = sorted(con, key=lambda ctr: cv2.boundingRect(ctr)[1])   # сорт.по (y)

cv2.drawContours(bi, con[570:750], -1, (216, 84, 227), 1)
cv2.drawContours(bi, con[1:240], -1, (2, 213, 1), 1)
cv2.drawContours(bi, con[240:570], -1, (5, 6, 225), 1)

cv2.imshow('Result', bi)
cv2.waitKey(0)
