import json

from flask import Flask, jsonify,request,g,Response
import re, requests
import json
from urllib.parse import unquote
from bs4 import BeautifulSoup
from smallgfw import *
from baziUtil import *
import json
import sys
import importlib
import os

app = Flask(__name__)

@app.before_request
def before_request():
    sensitive_folder_path = 'sensitive_words'
    g.sensitive_words = read_all_sensitive_words(sensitive_folder_path)


@app.route('/',methods=['GET'])
def index():
    # 接收查询参数
    param = request.args.get('param', default=None, type=str)
    # 返回参数和消息
    #return f'Received param: {param}'
    return f"Hello, World!{param}"




def initWords():
    path = 'sensitive_words/words.txt'
    fp = open(path, 'r',encoding='utf-8')
    word_list = []
    for line in fp:
        line = line[0:-1]
        word_list.append(line)
    fp.close()
    return word_list

def read_sensitive_words(file_path):
       sensitive_words = []
       with open(file_path, 'r', encoding='utf-8') as f:
           for line in f.readlines():
               word = line.strip()
               if word:
                   sensitive_words.append(word)
       return sensitive_words

def read_all_sensitive_words(folder_path):
       all_sensitive_words = []
       file_list = os.listdir(folder_path)
       for file in file_list:
           if file.endswith('.txt'):
               file_path = os.path.join(folder_path, file)
               words = read_sensitive_words(file_path)
               all_sensitive_words.extend(words)
       return all_sensitive_words



@app.route('/check', methods=['POST'])
def check():
    importlib.reload(sys)
    data =request.json
    getwords = data.get('words')
    print(f'违禁词检测：{getwords}')
    gfw = GFW()
    #words = initWords()
    #words =read_all_sensitive_words('./sensitive_words')
    words = g.sensitive_words
    gfw.set(words)  # 设置敏感词列表
    res = gfw.check(getwords)
    resp = {}
    resp['count'] = len(res)
    resp['datas'] = res
    #return json.dumps(resp)
    return resp



if __name__ == '__main__':
    app.run(debug=True)