# -*- coding=gbk -*-
# @author   : aoteman
# @time     : 2022/10/8 21:09

import os,sys

path = os.path.dirname(os.path.dirname(__file__))

sys.path.append(path) # ��ӵ���������

if __name__ == '__main__':
    from bin.JingDongProject import jing_dong_project

    jing_dong_project()