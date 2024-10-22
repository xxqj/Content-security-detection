# Content security detection

#### 介绍
小程序上线要求需要对文本输入内容检测，微信提供的api目前只能微信体系用需要openid，只有自己实现一个

#### 软件架构
软件架构说明
python 3


#### 安装教程

pip3 install flask

#### 使用说明
运行webApi.py

http://127.0.0.1:5000

#### 参与贡献
感谢以下开源项目

https://github.com/houbb/sensitive-word

https://github.com/caroltc/SensitivePy

#### 特技
小程序使用了这个文本检测，在线演示体验
![输入图片说明](%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20241022124303.jpg)

![输入图片说明](%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20241022124309.jpg)

这个只实现了文本检测，图片检测的话，可以参考uniapp实现微信安全检测的插件
https://ext.dcloud.net.cn/plugin?name=uni-sec-check
