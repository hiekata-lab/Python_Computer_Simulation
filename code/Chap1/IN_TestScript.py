# -*- coding: utf-8 -*-
# 標準画像データベースSIDBA(Standard Image Data-BAse)の表示
# 南カリフォルニア大学 http://sipi.usc.edu/database/
# 上記のサイトよりpeppers.jpgを入手
#
import cv2 # OpenCV3
file = "./data/peppers.jpg"
img = cv2.imread(file)
cv2.imshow("Pepper", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
