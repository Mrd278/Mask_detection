import os

folders = ['txt_files']
path = r'D:\\Mridul\\vkarma\\MaskDetection\\bbox_txt'


n = 601
for folder in folders:
    for image in os.scandir(folder):
        n+=1
        os.rename(image.path, os.path.join(path, '{:06}.txt'.format(n)))
