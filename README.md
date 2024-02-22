# easyocr-server
EasyOCR HTTP Server

## 模型下载
https://www.jaided.ai/easyocr/modelhub/

## Mac M1 安装 EasyOCR
```shell
# pytorch 安装 nightly 版本
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
pip2 install easyocr
```


### 非M1
```shell
pip3 install torch torchvision torchaudio
pip2 install easyocr
```