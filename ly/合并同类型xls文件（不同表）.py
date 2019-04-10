# -*- coding:utf-8 -*-
"""
JASON SYSU.EDU.CN
This is a Py script file.

"""
import pandas as pd
import os
# 获取表格列表
origin_file_list = os.listdir('C:/Users/Jas/Desktop/test')
print(origin_file_list)
# 循环遍历表格
writer = pd.ExcelWriter('C:/Users/Jas/Desktop/output.xlsx')
for i in origin_file_list:
    print(i)
    excel_file_name = i
    #拼接每个文件的路径
    file_path = 'C:/Users/Jas/Desktop/test/%s' % i
    print(file_path)
    # 读取文件内容
    content = pd.read_excel(file_path,dtype=str)
    sheet_name = i[:len(i) - 4]
    content.to_excel(writer, sheet_name, index=False)
writer.save()