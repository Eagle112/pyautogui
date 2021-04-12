import cv2 as cv
import numpy as np
 

if __name__ == "__main__":
    # 先把图片灰度处理。
    img = cv.imread('./img/test1.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
 
    template = cv.imread('./img/textSource.png')
    template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
    h, w = template.shape[:2]
 
    # 匹配
    result = cv.matchTemplate(template_gray,img_gray , cv.TM_CCOEFF_NORMED)
 
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print(max_val)
    print(min_val)
 
    # max_loc为左上角
    # 右下角
    right_bottom = (max_loc[0] + w, max_loc[1] + h)
 
    # 画矩形,红色的线框出来。
    cv.rectangle(img=img, pt1=max_loc, pt2=right_bottom, color=(0, 0, 255), thickness=3)
 
    cv.imshow('result', img)
    cv.waitKey(0)

