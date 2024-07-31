记录我对Yolov8模型的学习过程

***YOLO8***  
1、创建专用环境 py -m venv d:/yolo8venv  
2、pip install ultralytics  
3、下载cuda安装https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local  
4、pip uninstall torch torchvision  
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121  
5、下载https://www.dllme.com/dll/files/libomp140_x86_64/00637fe34a6043031c9ae4c6cf0a891d/download 放到system32目录  



***EISeg***   
pip install EiSeg  
报错，pip uninstall opencv-python ,然后安装低于4.x的版本 pip install opencv-python==3.x.x.x  
继续报错，pip install setuptools ,  
继续报错    pip install  paddlepaddle  
搞定  
Eiseg目前只能生成COCO格式的dataset，需要转换成YOLO格式。用https://github.com/Sheepy1977/myAiLearningMisc/blob/main/covert.py 
