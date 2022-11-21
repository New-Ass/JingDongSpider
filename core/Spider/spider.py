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
        """��ʼ�������"""
        # 1.����Edge�������������ڵ������ڴ�һ�����������
        options = EdgeOptions()
        options.add_arguments([r"--headless", r"--disable-gpu"]) # ��ͷ�����

        self.driver = webdriver.Edge(capabilities=options.to_capabilities())
        # self.driver = webdriver.Edge()

        # 2.ͨ������������������URL����
        self.driver.get(Settings.URL)

        sleep(Settings.SLEEP_TIME)

    def page_read(self):
        """��ҳԴ�����"""
        # ��ȡ��ʱ��ҳ��Դ��
        page = self.driver.page_source
        # xpath ����
        self.tree = etree.HTML(page)

    def search_goods(self):
        """������Ʒ���ƣ����������"""
        name_input = self.driver.find_element_by_id("key")
        name_input.send_keys(self.goods_name)
        sleep(Settings.SLEEP_TIME)

        # �������
        click = self.driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
        self.driver.execute_script('arguments[0].click()', click)
        sleep(Settings.SLEEP_TIME)

    def goods_message(self):
        """��ȡ��Ʒ��Ϣ"""
        """
        ��Ʒҳ��ҳѭ��
            ÿ��ѭ����ȡ��Ʒ�۸����Ƶ���Ϣ����Ҳ��һ��ѭ������Ϊһҳ�ж����Ʒ��
                ��ȡһ����Ʒ��Ϣ�󣨼�һ��ѭ����
                    ������Ʒ����ҳ��ȡ���ۣ����۷�ҳҲ��Ҫѭ��
        """
        # ����ʽ

        page = 1
        while page <= int(self.goods_page):
            print(page)
            # �������ظ�ҳ��������Ϣ
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(Settings.SLEEP_TIME)

            self.goods_price_name()

            self.page_read()

            page_list_length = len(self.tree.xpath('//*[@id="J_bottomPage"]/span[1]/a')) # ҳ�����ĳ��ȣ����һ������һҳ
            # �����һҳ
            next_page = self.driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[{}]'.format(page_list_length))
            self.driver.execute_script('arguments[0].click()', next_page)
            page += 1

    def goods_price_name(self):
        """��ȡ��Ʒ��Ϣ"""
        # ��ȡ��Ʒ�۸�

        self.page_read()

        length = len(self.tree.xpath('//*[@id="J_goodsList"]/ul/li')) # ��ȡ��ҳ��Ʒ����

        count = 1
        while count <= length:
            print(count)

            self.page_read()

            if len(self.tree.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[3]/strong/i/text()'.format(count))) != 0:
                self.goods_price = self.tree.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[3]/strong/i/text()'.format(count))[0]
            elif len(self.tree.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[2]/strong/i/text()'.format(count))) != 0:
                self.goods_price = self.tree.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[2]/strong/i/text()'.format(count))[0]
            print(self.goods_price)

            # ��ȡ��Ʒ����
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

            # ������Ʒ����ҳ��
            xpath = '//*[@id="J_goodsList"]/ul/li[{}]/div/div[1]/a'.format(count)
            good_detail = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script('arguments[0].click()', good_detail)
            sleep(Settings.SLEEP_TIME)

            self.comment()

            count += 1

    def comment(self):
        # ��ȡ��Ʒ����
        self.new_window()

        # �����ײ����ȴ����ۼ������
        comment_box = self.driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[5]')
        self.driver.execute_script('arguments[0].click()', comment_box)
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(Settings.SLEEP_TIME)

        self.page_read()
        for i in range(1, int(self.comment_page) + 1):
            self.page_read()
            if len(self.tree.xpath('//*[@id="comment-0"]/div[@class="comment-item"]')) == 0: # ���۹��ٻ�û�����ۣ�ֱ���˳�ѭ��
                break
            comment_counter = len(self.tree.xpath('//*[@id="comment-0"]/div[@class="comment-item"]'))
            count = 1
            while count <= comment_counter:
                self.page_read()
                self.content(count)
                count += 1

            # �����һҳ
            page_list_length = len(self.tree.xpath('//*[@id="comment-0"]/div[12]/div/div/a'))  # ҳ�����ĳ��ȣ����һ������һҳ
            # �����һҳ
            if page_list_length != 0:
                next_page = self.driver.find_element_by_xpath(
                    '//*[@id="comment-0"]/div[12]/div/div/a[{}]'.format(page_list_length))
                self.driver.execute_script('arguments[0].click()', next_page)
            else:
                self.close_window()
                break

        self.close_window()

    def new_window(self):
        # ��ȡ����,����Ϊһ���б�
        handles = self.driver.window_handles
        # ���һ�����´򿪵Ĵ��ڣ���ת���������
        self.driver.switch_to.window(handles[-1])

    def close_window(self):
        # �ر��´򿪵Ĵ���
        self.driver.close()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    def content(self, count):
        # ��ȡ��ʱ��ҳ��Դ��
        self.page_read()

        # �û���
        username = self.tree.xpath('//*[@id="comment-0"]/div[{}]/div[1]/div[1]/text()'.format(count))[1].strip(" ")

        # �Ƿ��ǻ�Ա
        huiyuan = self.tree.xpath('//*[@id="comment-0"]/div[{}]/div[1]/div[2]/a/text()'.format(count))
        if len(huiyuan) == 0:
            huiyuan = "None"
        else:
            huiyuan = huiyuan[0]

        # ��������
        content = self.tree.xpath('//*[@id="comment-0"]/div[{}]/div[2]/p/text()'.format(count))[0]

        # �Ǽ�
        star = self.tree.xpath('//*[@id="comment-0"]/div[{}]/div[2]/div[1]/@class'.format(count))[0][-5:]

        # print(star)

        with open(Settings.DOWNLOAD_PATH, "a", encoding="utf-8")as f:
            f.write(self.goods_name + "|" + self.goods_price + "|" + username + "|" + huiyuan + "|" + star + "|" + content)
            f.write("\n")

    def Paixu(self):
        dic = {
            "�ۺ�": 1,
            "����": 2,
            "������": 3,
            "��Ʒ": 4
        }
        num = dic.get(self.paixu)
        xpath = '//*[@id="J_filter"]/div[1]/div[1]/a[{}]'.format(num)
        sales_count = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script('arguments[0].click()', sales_count)
        sleep(Settings.SLEEP_TIME)