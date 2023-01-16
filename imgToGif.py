# 作者：OpenCv机器视觉
# 时间：2023/1/4
# 功能：图片转GIF
import imageio
import os

def img_to_gif(imgs, gif_name, duration=1.0):

    # 将所有图片存放在同一个列表当中
    frames = []
    for img in imgs:
        print(img)
        frames.append(imageio.imread(img))

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)


def main():
    file_path = ".\\img\\lnx"        # 文件夹路径，这里是用相对路径表示
    imgs = os.listdir(file_path)    # 获取文件夹所有的图片名称

    # 图片文件路径+图片名称拼接成完整的相对路径
    imgs_path = []
    for j,img in enumerate(imgs):
         imgs_path.append(os.path.join(file_path,img))


    gif_name = '1.gif'
    duration = 0.2       # 帧率 = 1/duration
    img_to_gif(imgs_path, gif_name, duration)   # 开始图片转GiF



if __name__ == '__main__':
    main()
