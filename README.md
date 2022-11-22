# JingDongSpider

## 项目简单介绍
这是一个简单的京东网站的爬虫项目，使用 PyQt5 模块构建简单的 UI 界面

## 一些文件参数介绍
### ```Settings.py```
```python
URL = "https://www.jd.com/" # 不要更改，参数代表 京东主页 的网址
SLEEP_TIME = 1 # 程序响应时爬虫在某些阶段的 sleep 时间，避免被京东封 IP，可以修改
DOWNLOAD_PATH = r'' # 爬取保存的 txt 文件在本地的 保存路径
EXCEL_PATH = r"" # 将 txt 文件转换为 .xls 文件后在本地的保存路径
```

## 项目运行
运行之前确保所有的 文件 保存在一个文件夹下，运行时只需要运行 main.py 文件

## Brief Introduction of the Project
（由于本人英语水平有限，以下内容基本上是机器翻译）
（Due to my limited English proficiency, the following content is basically machine translation）

This is a simple crawler project of JD website, using PyQt5 module to build a simple UI interface

## Some file parameters are introduced
### ```Settings.py```
```python
URL = "https://www.jd.com/" # Do not change, the parameter represents the website address of the JD.com homepage
SLEEP_TIME = 1 # Program response crawler in some stages of sleep time, to avoid being JD.com sealed IP, can be modified
DOWNLOAD_PATH = r'' # Crawl to save the txt file in the local saving path
EXCEL_PATH = r"" # After the txt file is converted to an.xls file, the.xls file is saved in the local directory
```

## project running
Make sure all files are saved in a folder before running, and only need to run main.py files when running
