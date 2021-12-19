import os
import cv2
import time

#img_root = "./test_img/0000"
#img_root = "./test_img/00"
#path="./test_img/"
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # mp4

dirlist=os.listdir()
fps = 30
size=(256,256)

for dirs in dirlist:
    if os.path.isdir(dirs):
        img_root = "./" + dirs
        out_path = dirs + ".mp4"
        print(img_root)
        print(out_path)
        videoWriter = cv2.VideoWriter(out_path, fourcc, fps, size)
        files = os.listdir(dirs)
        numfiles = len(files)
        print(numfiles)
        for i in range(numfiles):
            if i < 10:
                img_path = img_root + "/0000"
            elif i < 100:
                img_path = img_root + "/000"
            else:
                img_path = img_root + "/00"
            print(img_path + str(i) + ".jpg")
            frame = cv2.imread(img_path + str(i) +'.jpg')
            videoWriter.write(frame)
        videoWriter.release()

        


#file_path='saveVideo.mp4' # 导出路径DIVX/mp4v
#
##可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
# #fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # avi
#fourcc = cv2.VideoWriter_fourcc(*'mp4v') # mp4
#
#videoWriter = cv2.VideoWriter(file_path,fourcc,fps,size)
#
#for i in range(150):
#    if i < 10 :
#        path = img_root + "00"
#    elif i < 100:
#        path = img_root + "0"
#    else:
#        path = img_root
#    print(path + str(i))
#    frame = cv2.imread(path+str(i)+'.jpg')
#    videoWriter.write(frame)
#
#
#videoWriter.release() #释放
