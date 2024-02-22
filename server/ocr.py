# -*- coding: utf-8 -*-

# ocr 工具函数
import os
import numpy as np

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

def result_json(result):
    # 构建 JSON 对象
    output = []
    for index, detection in enumerate(result):
        if not detection or len(detection) < 2:
            continue
        text = detection[1]
        confidence = detection[2]
        data = {
            "index": index,
            "text": text,
            "confidence": confidence
        }
        coordinates_val = detection[0]
        if coordinates_val and len(coordinates_val) == 4:
            data["top_left"] = [int(np.int64(coordinates_val[0][0])),int(np.    int64(coordinates_val[0][1]))]
            data["top_right"] = [int(np.int64(coordinates_val[1][0])),int(np.   int64(coordinates_val[1][1]))]
            data["bottom_right"] = [int(np.int64(coordinates_val[2][0])),int    (np.int64(coordinates_val[2][1]))]
            data["bottom_left"] = [int(np.int64(coordinates_val[3][0])),int(np. int64(coordinates_val[3][1]))]

        output.append(data)
    return output