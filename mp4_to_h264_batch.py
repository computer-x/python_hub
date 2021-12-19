import os

dirlist = os.listdir()

for files in dirlist:
    #print(files)
    partname = os.path.splitext(files)
    #print(partname)
    outname = partname[0] + ".h264"
    #print(outname)
    cmd = "ffmpeg -i "
    cmd += files
    cmd += " -f h264 "
    cmd += outname
    print(cmd)

    os.system(cmd)
# ffmpeg -i xxx.mp4 -f h264 xxx.h264
