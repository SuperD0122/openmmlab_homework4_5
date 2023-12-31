import cv2


def handl_Canny(pic_path='mypicture.jpg'):
    #读取图像
    img=cv2.imread(pic_path)
    #缩放图像的大小
    img=cv2.resize(src=img,dsize=(512,512))
    #对图像进行边缘检测，低阈值=50 高阈值=200
    img_canny=cv2.Canny(img,threshold1=50,threshold2=200)
    #显示检测之后的图像
    cv2.imshow('image',img_canny)
    #显示原图像
    cv2.imwrite('mypicture_canny.jpg',img_canny)
    cv2.imshow('src',img)
    cv2.waitKey(0)

#销毁所有的窗口
cv2.destroyAllWindows()
if __name__ == '__main__':

    handl_Canny()
