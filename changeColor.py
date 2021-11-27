import cv2
from PIL import Image
import random
import os
import random as rand


# 随机生成颜色
def paste(bac, fore):
    for i in range(0, 1000, 250):
        for j in range(0, 900, 250):
            bac.paste(fore, (i, j), fore)
    # 贴图 子图母图保存地址
    base_path = "images/pics\\"
    path_img = base_path + str(rand.randint(9, 100000)).zfill(8) + ".png"
    bac.save(path_img)
    return bac


def change(logo_path):
    num = 0  # 读取的图片序号
    num_max = 6  # 图片总数量
    hue_change = 10  # 色调改变值 步长
    count = 0  # 记录每张图片生成的数量
    # 图片存储地址

    img_name = logo_path + '/%s.png' % str(num + 1)
    img = cv2.imread(img_name, cv2.IMREAD_COLOR)  # 打开文件

    # 通过cv2.cvtColor把图像从BGR转换到HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    turn_green_hsv = img_hsv.copy()
    # 色调hue变化范围5——50
    for i in range(1, 6):
        # 生成的图片数目
        turn_green_hsv[:, :, 0] = (turn_green_hsv[:, :, 0] + hue_change * i) % 180
        turn_green_img = cv2.cvtColor(turn_green_hsv, cv2.COLOR_HSV2BGR)
        out_path = "images/out"
        cv2.imwrite(out_path+'/%s_%s.png' % (str(num + 1), str(count + 1)),
                    turn_green_img)
        print("successfully save %s_%s pic" % (str(num + 1), str(count + 1)))
        count += 1

    if num == num_max - 1:
        exit(0)

    count = 0
    num += 1
    return out_path  #改变颜色的logo输出路径


def lucency(path):
    dir_names = os.listdir(path)  # 生成图片列表
    # print(dir_names)
    for dir in dir_names:
        new_path = os.path.join(path, dir)
        img = Image.open(new_path)
        img = img.convert('RGBA')  # 修改颜色通道为RGBA
        width, height = img.size
        array = img.load()  # 获取图片像素操作入口
        for i in range(width):
            for j in range(height):
                pos = array[i, j]  # 获得某个像素点，格式为(R,G,B,A)元组
                # 如果R G B三者都大于240(很接近白色了，数值可调整)
                isEdit = (sum([1 for x in pos[0:3] if x > 240]) == 3)
                if isEdit:
                    # 更改为透明
                    array[i, j] = (255, 255, 255, 0)
        base_path = "images/tt\\"
        path_img = base_path + str(random.randint(9, 100000)).zfill(8) + ".png"
        img.save(path_img)  # 要保存为.PNG格式的图片才可以


# 用户输入
# def myrun(logo_path):
#     logo_path = ""
#     change()  # 改变颜色
#     path = r'C:\Python\PycharmProjects\tt\images\out'
#     lucency(path)  # 透明
#
#     path = "images/mt"  # 母图
#     dir_names = os.listdir(path)  # 生成图片列表
#     spath = "images/tt"  # 粘贴子图路径
#     dir_name = os.listdir(spath)
#     for file in dir_name:
#         newpath = os.path.join(spath, file)
#         foreground = Image.open(newpath)
#         foreground = foreground.convert("RGBA")
#         for dir in dir_names:
#             new_path = os.path.join(path, dir)
#             background = Image.open(new_path)
#             paste(background, foreground)
#     return outpath


if __name__ == '__main__':
    logo_path = r"C:\Python\PycharmProjects\tt\images\in"
    path = change(logo_path)  # 改变颜色
    lucency(path)  # 透明

    path = "images/mt"  # 母图
    dir_names = os.listdir(path)  # 生成图片列表
    spath = "images/tt"  # 粘贴子图路径
    dir_name = os.listdir(spath)
    for file in dir_name:
        newpath = os.path.join(spath, file)
        foreground = Image.open(newpath)
        foreground = foreground.convert("RGBA")
        for dir in dir_names:
            new_path = os.path.join(path, dir)
            background = Image.open(new_path)
            paste(background, foreground)

'''
#遍历图片 将图片变成透明色

path = "images/out"
def lucency(p):
    dir_names = os.listdir(path)  # 生成图片列表
    #print(dir_names)
    for dir in dir_names:
        new_path = os.path.join(path, dir)
        img = Image.open(new_path)
        img = img.convert('RGBA')  # 修改颜色通道为RGBA
        width, height = img.size
        array = img.load()  # 获取图片像素操作入口
        for i in range(width):
            for j in range(height):
                pos = array[i, j]  # 获得某个像素点，格式为(R,G,B,A)元组
                # 如果R G B三者都大于240(很接近白色了，数值可调整)
                isEdit = (sum([1 for x in pos[0:3] if x > 240]) == 3)
                if isEdit:
                    # 更改为透明
                    array[i, j] = (255, 255, 255, 0)
        base_path = "images/tt\\"
        path_img = base_path + str(random.randint(9, 100000)).zfill(8) + ".png"
        img.save(path_img)  # 要保存为.PNG格式的图片才可以
lucency(path)
'''
