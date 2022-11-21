# -*- coding=gbk -*-
# @author   : aoteman
# @time     : 2022/10/12 20:16

# -*- coding=gbk -*-
# @author   : aoteman
# @time     : 2022/9/24 22:03

import os,sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(path)

if __name__ == '__main__':
    from conf.Settings import DOWNLOAD_PATH,EXCEL_PATH
    from openpyxl import Workbook

    book = Workbook()
    sheet = book.active

    title = ("goods_name", "price", "username", "huiyuan", "star", "comment content")

    sheet.append(title)

    if os.path.isfile(DOWNLOAD_PATH):
        with open(DOWNLOAD_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line_list = line.split("|")
                # self.goods_name + | + price + "|" + username + "|" + huiyuan + "|" + star + "|" + content
                sheet.append(line_list)

        book.save(EXCEL_PATH)

        print("over!!!")
    else:
        print("can't find the DOANLOAD file!!!")