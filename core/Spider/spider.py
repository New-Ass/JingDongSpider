# -*- coding=gbk -*-
# @author   : aoteman
# @time     : 2022/10/9 20:51

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.EdgeOptions import EdgeOptions
from conf import Settings
from time import sleep
from lxml import etree
import os

class Spider:
    def __init__(self, goods_name, paixu, goods_page, comment_page):
        self.goods_name = goods_name
        self.paixu = paixu
        self.goods_page = goods_page
        self.comment_page = comment_page

        self.run()

    def run(self):
        self.start_web()

        self.search_goods()

        self.Paixu()

        self.goods_message()

        self.driver.close()

    def start_web(self):
        """初始化浏览器"""
        # 1.创建Edge浏览器对象，这会在电脑上在打开一个浏览器窗口
        options = EdgeOptions()
        options.add_arguments([r"--headless", r"--disable-gpu"]) # 无头浏览器

        self.driver = webdriver.Edge(capabilities=options.to_capabilities())
        # self.driver = webdriver.Edge()

        # 2.通过浏览器向服务器发送URL请求
        self.driver.get(Settings.URL)

        sleep(Settings.SLEEP_TIME)

    def page_read(self):
        """网页源码解析"""
        # 获取此时的页面源码
        page = self.driver.page_source
        # xpath 解析
        self.tree = etree.HTML(page)

    def search_goods(self):
        """输入商品名称，并点击搜索"""
        name_input = self.driver.find_element_by_id("key")
        name_input.send_keys(self.goods_name)
        sleep(Settings.SLEEP_TIME)

        # 点击搜索
        click = self.driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
        self.driver.execute_script('arguments[0].click()', click)
        sleep(Settings.SLEEP_TIME)

    def goods_message(self):
        """获取商品信息"""
        """
        商品页翻页循环
            每次循环获取商品价格、名称等信息（这也是一个循环，因为一页有多个商品）
                获取一个商品信息后（即一个循环后）
                    进入商品详情页获取评论，评论翻页也需要循环
        """
        # 排序方式

        page = 1
        while page <= int(self.goods_page):
            print(page)
            # 滚动加载该页面所有信息
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(Settings.SLEEP_TIME)

            self.goods_price_name()

            self.page_read()

            page_list_length = len(self.tree.xpath('//*[@id="J_bottomPage"]/span[1]/a')) # 页数条的长度，最后一个是下一页
            # 点击下一页
            next_page = self.driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[{}]'.format(page_list_length))
            self.driver.execute_script('arguments[0].click()', next_page)
            page += 1

    def goods_price_name(self):
        """爬取商品信息"""
        # 获取商品价格

        self.page_read()

        length = len(self.tree.xpath('//*[@id="J_goodsList"]/ul/li')) # 获取该页商品数量

        count = 1
        while count <= length:
            print(count)

            self.page_read()

            if len(self.tree.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[3]/strong/i/text()'.format(count))) != 0:
                self.goods_price = self.tree.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[3]/strong/i/text()'.format(count))[0]
            elif len(self.tree.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[2]/strong/i/text()'.format(count))) != 0:
                self.goods_price = self.tree.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[2]/strong/i/text()'.format(count))[0]
            print(self.goods_price)

            # 获取商品名称
            # //*[@id="J_goodsList"]/ul/li[1]/div/div[4]/a/em
            # //*[@id="J_goodsList"]/ul/li[1]/div/div[3]/a/em
            if len(self.tree.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[4]/a/em/text()'.format(count))) != 0:
                self.goods_name = self.tree.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[4]/a/em/text()'.format(count))
            elif len(self.tree.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[3]/a/em/text()'.format(count))) != 0:
                self.goods_name = self.tree.xpath(
                    '//*[@id="J_goodsList"]/ul/li[{}]/div/div[3]/a/em/text()'.format(count))

            num = ""
            for i in self.goods_name:
                i = i.replace(" ", "")
                i = i.replace("\n", "")
                i = i.replace("\t", "")
                num += i
            self.goods_name = num
            print(self.goods_name)

            # 进入商品详情页面
            xpath = '//*[@id="J_goodsList"]/ul/li[{}]/div/div[1]/a'.format(count)
            good_detail = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script('arguments[0].click()', good_detail)
            sleep(Settings.SLEEP_TIME)

            self.comment()

            count += 1

    def comment(self):
        # 获取商品评论
        self.new_window()

        # 滑到底部，等待评论加载完成
        comment_box = self.driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[5]')
        self.driver.execute_script('arguments[0].click()', comment_box)
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(Settings.SLEEP_TIME)

        self.page_read()
        for i in range(1, int(self.comment_page) + 1):
            self.page_read()
            if len(self.tree.xpath('//*[@id="comment-0"]/div[@class="comment-item"]')) == 0: # 评论过少或没有评论，直接退出循环
                break
            comment_counter = len(self.tree.xpath('//*[@id="comment-0"]/div[@class="comment-item"]'))
            count = 1
            while count <= comment_counter:
                self.page_read()
                self.content(count)
                count += 1

            # 点击下一页
            page_list_length = len(self.tree.xpath('//*[@id="comment-0"]/div[12]/div/div/a'))  # 页数条的长度，最后一个是下一页
            # 点击下一页
            if page_list_length != 0:
                next_page = self.driver.find_element_by_xpath(
                    '//*[@id="comment-0"]/div[12]/div/div/a[{}]'.format(page_list_length))
                self.driver.execute_script('arguments[0].click()', next_page)
            else:
                self.close_window()
                break

        self.close_window()

    def new_window(self):
        # 获取窗口,返回为一个列表
        handles = self.driver.window_handles
        # 最后一个是新打开的窗口，跳转到这个窗口
        self.driver.switch_to.window(handles[-1])

    def close_window(self):
        # 关闭新打开的窗口
        self.driver.close()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    def content(self, count):
        # 获取此时的页面源码
        self.page_read()

        # 用户名
        username = self.tree.xpath('//*[@id="comment-0"]/div[{}]/div[1]/div[1]/text()'.format(count))[1].strip(" ")

        # 是否是会员
        huiyuan = self.tree.xpath('//*[@id="comment-0"]/div[{}]/div[1]/div[2]/a/text()'.format(count))
        if len(huiyuan) == 0:
            huiyuan = "None"
        else:
            huiyuan = huiyuan[0]

        # 评价内容
        content = self.tree.xpath('//*[@id="comment-0"]/div[{}]/div[2]/p/text()'.format(count))[0]

        # 星级
        star = self.tree.xpath('//*[@id="comment-0"]/div[{}]/div[2]/div[1]/@class'.format(count))[0][-5:]

        # print(star)

        with open(Settings.DOWNLOAD_PATH, "a", encoding="utf-8")as f:
            f.write(self.goods_name + "|" + self.goods_price + "|" + username + "|" + huiyuan + "|" + star + "|" + content)
            f.write("\n")

    def Paixu(self):
        dic = {
            "综合": 1,
            "销量": 2,
            "评论数": 3,
            "新品": 4
        }
        num = dic.get(self.paixu)
        xpath = '//*[@id="J_filter"]/div[1]/div[1]/a[{}]'.format(num)
        sales_count = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script('arguments[0].click()', sales_count)
        sleep(Settings.SLEEP_TIME)