# -*- coding: utf-8 -*-
# by：Apsinc
# time：2019年12月10日
#Python实现将一张图片放到另一张图片指定的位置上并合成一张图
import os
import random

import PIL as plt
from PIL import Image

'''
path = "huoche.jpg"#母图详细文件名以及路径
img = Image.open(path)
# img = qr.make_image(fill_color="#555555", back_color="Red")
img = img.convert("RGBA")  # CMYK/RGBA 转换颜色格式（CMYK用于打印机的色彩，RGBA用于显示器的色彩）
# 添加子图
icon = Image.open("1.png")#子图文件名
# 获取图片的宽高
img_w, img_h = img.size#获取被放图片的大小（母图）
icon_w,icon_h=icon.size#获取小图的大小（子图）
factor = 6
size_w = int(img_w / factor)
size_h = int(img_h / factor)
icon_w, icon_h = icon.size
#防止子图尺寸大于母图
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
# # 重新设置子图的尺寸
# icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
# 粘贴图片
img.paste(icon, (w, h), mask=None)
# 保存图片
img.save("picture/c.png")#合成后的图片路径以及文件名
from PIL import Image

#调节图片透明度
def transparence2white(img):
    #     img=img.convert('RGBA')  # 此步骤是将图像转为灰度(RGBA表示4x8位像素，带透明度掩模的真彩色；CMYK为4x8位像素，分色等)，可以省略
    sp = img.size
    width = sp[0]
    height = sp[1]
    print(sp)
    for yh in range(height):
        for xw in range(width):
            dot = (xw, yh)
            color_d = img.getpixel(dot)  # 与cv2不同的是，这里需要用getpixel方法来获取维度数据
            if (color_d[3] == 0):
                color_d = (0, 255, 255, 255)
                img.putpixel(dot, color_d)  # 赋值的方法是通过putpixel
    return img

'''

#图片、贴图 bac ，母图  ；fore ，子图
def paste(bac,fore):
    for i  in range(0,1000,250):
        for j in range(0,900,250):
          bac.paste(fore, (i, j), fore)
    base_path = "images/pic\\"
    path_img = base_path + str(random.randint(9, 100000)).zfill(8) + ".png"
    bac.save(path_img)
    return bac


'''if __name__ == '__main__':
   
    foreground = Image.open("tmtu.png")
    paste(background,foreground)

def produce_img():
    base_dir = "C:\python file\SBRB\picture"
    files = os.listdir(base_dir)
    for i in files:
        # 打印图片
        new_path = os.path.join(path, i)
        background = Image.open(new_path)


    return path_img


foreground = "images/tt"
def open(fo):
    dir_name=os.listdir(fo)
    for d in dir_name:
        newpath=os.path.join(fo,d)
        fo=Image.open(newpath)
'''

if __name__ == '__main__':
    path="images/mt"  #母图
    #foreground = Image.open("tmtu.png")
    #foreground=""#子图路径
    dir_names=os.listdir(path) #生成图片列表
    #print(dir_names)
    #background=produce_img()
    spath="images/tt" #粘贴子图路径
    dir_name=os.listdir(spath)
    for file in dir_name:
        newpath=os.path.join(spath,file)
        foreground=Image.open(newpath)
        foreground = foreground.convert("RGBA")
        for dir in dir_names:
          new_path = os.path.join(path,dir)
          background = Image.open(new_path)
       # plt.imshow(background)
        #plt.show()
        #background = background.convert("RGBA")
        #foreground = foreground.convert("RGBA")
          paste(background, foreground)








