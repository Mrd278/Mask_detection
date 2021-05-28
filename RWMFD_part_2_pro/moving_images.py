import os

missing = [116, 85, 140, 141, 144, 151, 155, 157, 158, 159, 161, 174, 179, 181, 183, 191, 197, 203]
folders = []
for i in range(209):
   if i not in missing:
       folders.append('{:05}'.format(i))

path = r'D:\\Mridul\\vkarma\\MaskDetection\\Images'


try:
    n = 0
    for folder in folders:
        for image in os.scandir(folder):
            n+=1
            os.rename(image.path, os.path.join(path, '{:06}.jpg'.format(n)))
except:
    print('error occured')
