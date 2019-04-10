# 标题:      dbf转xlsx
# 描述:      dbf文件批量转xlsx
# 作者:      Jas
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# 调用模块
import pandas as pd
from dbfread import DBF
from pandas import DataFrame
import os.path
import os
def dbfToxlsx():
    #需要转换的dbf文件存放处
    rootdir = r"data dir" 
    files = os.listdir(rootdir)
    #列出dbf文件夹下的所有文件
    num = len(files)
    for i in range(num):
        #得到扩展名是否为dbf>分离文件名与扩展名，返回(f_name, f_extension)元组
        kname = os.path.splitext(files[i])[1]
        #判定扩展名是否为xls,屏蔽其它文件
        if kname == '.dbf':
            #得到全路径的文件dbf>合成需要转换的路径与文件名
            fname = rootdir + '\\' + files[i]
            #打开需要转换的文件
            wb = DBF(fname,encoding='gbk')
            frame = DataFrame(iter(wb),dtype=str)
            #输出文件名称
            writer= rootdir + '\\' + os.path.splitext(files[i])[0] + ".xlsx" 
            frame.to_excel(writer,index=None)
            print("-----ojbk------")
if __name__ == '__main__':
    dbfToxlsx()