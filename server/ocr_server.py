# -*- coding: utf-8 -*-

import easyocr
import json
import ocr

from flask import Flask, request, jsonify, make_response

# 创建Flask应用程序实例
app = Flask(__name__)
app.config.from_file('ocr_server_cfg.json', load=json.load)
# 创建 EasyOCR 实例
ocr_reader = easyocr.Reader(['ch_sim','en'], gpu=app.config['USE_GPU'])

# 定义路由和对应的视图函数
@app.route('/health')
def health():
    return 'ocr server ok!'

@app.route('/ocr/image_path', methods=['POST'])
def ocr_image_path():
    req_data = request.get_json()
    image_path = req_data['image_path']
    check_err =  ocr.validate_image(image_path)
    if check_err:
        return make_response(f'image check err {check_err}', 400)
    result = ocr_reader.readtext(image_path)
    return jsonify(ocr.result_json(result))

# 运行应用程序，指定自定义端口
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=app.config['PORT'])