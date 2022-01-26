# python_hub
保存了一些以后可能还会用到的python工具脚本


关于cv：
* 安装命令是：pip3 install opencv-python
      安装时会提示：No module named 'skbuild'
* 安装命令为：pip3 install scikit-build
      后续安装过程中又会报错：Problem with the CMake installation, aborting build. CMake executable is cmake
* 在ubuntu18.04中不要通过pip来安装cmake，要通过apt来安装cmake：sudo apt install cmake
      此后即可完成opencv-python的安装。
