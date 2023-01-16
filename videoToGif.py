# 作者：OpenCv机器视觉
# 时间：2023/1/4
# 功能：视频转图片
import cv2 as cv
import os

input_path= "1.mp4"

name =  os.path.splitext(input_path)[0]  # 文件名称


cap = cv.VideoCapture(input_path)

# 检车保存路径在不在，如果没有output文件就自己创建一个
if os.path.exists(name):
    pass
else:
    os.makedirs(name)


i = 0 # 图片编号初始值设置
while True:
    ret,frame = cap.read()
    i = i+1
    if i%3==0:  # 没3帧获取一张图片
        print(i)
        cv.imwrite(".\\"+name+"\\"+str(format(i, '04d'))+".jpg",frame)# 对图片进行保存
