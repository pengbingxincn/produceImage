import os
import random as rand
from PIL import Image

def paste(bac,fore):
    for i  in range(0,1000,250):
        for j in range(0,900,250):
          bac.paste(fore, (i, j), fore)
    #贴图 子图母图保存地址
    base_path = "images/pic\\"
    path_img = base_path + str(rand.randint(9, 100000)).zfill(8) + ".png"
    bac.save(path_img)
    return bac




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
#旋转

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
def horizontal_flip(image_path):
    im = Image.open(image_path)
    out = choose_transpose(im, 4)#rand.randint(0,4)
    out.save(image_path)
    return out
#horizontal_flip("images/out/1_5.png")