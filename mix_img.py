# -*- coding: utf-8 -*-
# by：Apsinc
# time：2019年12月10日
# Python实现将一张图片放到另一张图片指定的位置上并合成一张图
from PIL import Image
import random
import os
import torch
import cv2

path = "J:\yoloWorlplace\\trademarkDetection\\test\\testImg\mt.jpeg"  # 母图详细文件名以及路径

test_img_path = "J:\yoloWorlplace\\trademarkDetection\\test\\tmtu.png"
test_img_path2 = "J:\yoloWorlplace\\trademarkDetection\\test\\tmtu1.png"


# 透明贴图
def paste(bac, fore):

    base_path = r"J:\data\produce"
    for i in range(0, 1000, 250):
        for j in range(0, 900, 250):
            bac.paste(fore, (i, j), fore)
            path_img = base_path + str(random.randint(9, 100000)).zfill(8) + ".png"
            # path_img = "J:\data\c.png"
            bac.save(path_img)
    return path_img


# 贴图
def mix_one_img(path, icon_path):
    img = Image.open(path)
    img = img.convert("RGBA")  # CMYK/RGBA 转换颜色格式（CMYK用于打印机的色彩，RGBA用于显示器的色彩）
    # 添加子图
    icon = Image.open(icon_path)  # 子图文件名
    # 获取图片的宽高
    img_w, img_h = img.size  # 获取被放图片的大小（母图）
    icon_w, icon_h = icon.size  # 获取小图的大小（子图）
    factor = 6
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    # 防止子图尺寸大于母图
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # # 重新设置子图的尺寸
    # icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    for i in range(0, 3):
        w = int((img_w - icon_w) / random.uniform(0, 9))
        h = int((img_h - icon_h) / random.uniform(0, 9))
        # 粘贴图片
        img.paste(icon, (w, h), mask=None)
    # 保存图片
    base_path = "J:\photo\data\productData_lining\\train\images\\"
    path_img = base_path + str(random.randint(9, 100000)).zfill(8) + ".png"
    # img = horizontal_flip(path_img)
    img.save(path_img)  # 合成后的图片路径以及文件名
    print(path_img)
    return path_img


# 批量贴图
def produce_img(icon_path):
    base_dir = r"J:\data\bac"
    files = os.listdir(base_dir)
    for i in files:
        change_size(test_img_path)
        horizontal_flip(test_img_path)
        path_img = base_dir + "\\" + i
        horizontal_flip(paste(Image.open(path_img), Image.open(icon_path)))
        print(path_img)


def horizontal_flip(image_path):
    im = Image.open(image_path)
    out = choose_transpose(im, Image.ROTATE_90)
    out.save(image_path)
    return out


# 改变商标的大小，缩小或者扩大
def change_size(img_path):
    img = cv2.imread(img_path)
    img_shape = img.shape
    high = img_shape[0]
    width = img_shape[1]
    w = random.uniform(0.1, 3)
    if high > 400:
        high = width = 200
    size = (int(width / w), int(high / w))
    img = cv2.resize(img, size)
    test_img_path2 = "J:\yoloWorlplace\\trademarkDetection\\test\\tmtu1.png"
    cv2.imwrite(test_img_path2, img)
    return img


# 旋转
def choose_transpose(im, i):
    if i == 0:
        out = im.transpose(Image.FLIP_LEFT_RIGHT)
    if i == 1:
        out = im.transpose(Image.FLIP_TOP_BOTTOM)
    if i == 2:
        out = im.transpose(Image.ROTATE_90)
    if i == 3:
        out = im.transpose(Image.ROTATE_180)
    if i == 4:
        out = im.transpose(Image.ROTATE_270)
    return out


# 调整图片的透明度
def lucency(path):
    img = Image.open(path)
    img = img.convert('RGBA')  # 修改颜色通道为RGBA
    x, y = img.size  # 获得长和宽
    # 设置每个像素点颜色的透明度
    for i in range(x):
        for k in range(y):
            color = img.getpixel((i, k))
            color = color[:-1] + (100,)
            img.putpixel((i, k), color)
    img.save("tologo.png")  # 要保存为.PNG格式的图片才可以


if __name__ == '__main__':

    # produce_img(test_img_path2)
    # background = Image.open("J:\yoloWorlplace\\trademarkDetection\data\images\\00004063.jpg")
    # foreground = Image.open("J:\yoloWorlplace\\trademarkDetection\\test\\tmtu.png")
    #
    # print(paste(background, foreground))
    horizontal_flip(r"J:\yoloWorlplace\\trademarkDetection\\test\\tmtu2.png")