记录我对Yolov8模型的学习过程

***YOLO8***  
1、创建专用环境 `py -m venv d:/yolo8venv`  
2、`pip install ultralytics`  
3、下载cuda安装https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local  
4、`pip uninstall torch torchvision`  然后 
`pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`  
5、下载https://www.dllme.com/dll/files/libomp140_x86_64/00637fe34a6043031c9ae4c6cf0a891d/download 放到system32目录  



***EISeg***   
`pip install EiSeg`  
报错，`pip uninstall opencv-python` ,然后安装低于4.x的版本 `pip install opencv-python==3.x.x.x`  
继续报错，`pip install setuptools` ,  
继续报错    `pip install  paddlepaddle`  
搞定  
Eiseg目前只能生成COCO格式的dataset，需要转换成YOLO格式。用https://github.com/Sheepy1977/myAiLearningMisc/blob/main/covert.py 

***SAM2***  
安装SAM2遇到的一些坑：  
1. https://pytorch.org/get-started/locally/ 必须从这里获得pip install 代码以正确安装torch（先安装对应的CUDA TOOLKIT）  
2. git clone https://github.com/facebookresearch/segment-anything-2.git  （clone git仓库）  
3. cd segment-anything-2;  切换当前目录到sam2  
4. 手动设置CUDA_HOME系统变量为C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1  注意，设置完需要重启系统才能完成。  
5. 如果直接pip install -e . 尝试使用pip install --no-build-isolation -e .
6. 如报错，pip install wheel  
7. 完成安装 (未解决）  
