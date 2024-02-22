# -*- coding: utf-8 -*-

# ocr 工具函数
import os

# 验证图片是否符合要求
def validate_image(image_path):
    # image_path 必须是已/开头
    if not image_path.startswith('/'):
        return 'image path must start with /'
    # image_path 结尾必须是 png 或 jpg 或 jpeg
    if not image_path.endswith('.png') and not image_path.endswith('.jpg') and not image_path.endswith('.jpeg'):
        return 'image path must end with .png or .jpg or .jpeg'
    # Check if the file exists
    if not os.path.exists(image_path):
        return 'image file not exists'
    # check file size
    if os.path.getsize(image_path) > 1024 * 1024 * 4:
        return 'image file size should less than 4M'
    return None