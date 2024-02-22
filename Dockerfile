# 使用Ubuntu 20.04作为基础镜像
FROM ubuntu:20.04
# 设置时区为UTC
ENV TZ=UTC
# 设置环境变量，用于避免与用户交互的情况
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# 更新apt源并安装必要的软件包
RUN apt-get update && apt-get install -y \
    vim \
    wget \
    bzip2 \
    ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    libxrender-dev \
    libgl1-mesa-dev \
    python3.10 \
    python3-pip \
    git

# 切换pip源到清华大学镜像源
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 解决 pytorch 安装依赖问题
RUN pip3 install networkx==3.1

# 安装PyTorch CPU版本
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
# 安装 easyocr
RUN pip3 install easyocr
# 安装 Flask
RUN pip3 install Flask

# 设置工作目录
WORKDIR /app

# easyocr 源码安装
# RUN mkdir -p /home
# COPY ./EasyOCR /home/EasyOCR

# RUN cd /home/EasyOCR \
#     && python setup.py build_ext --inplace -j 4 \
#     && python -m pip3 install -e .  \
#     && pip3 install --force-reinstall -v "Pillow==9.5.0"

COPY ./model /root/.EasyOCR/model
COPY ./server /app/server

# 运行ocr_server.py
CMD [ "python3", "/app/server/ocr_server.py" ]