# 标题:     dbf转xlsx
# 描述:      dbf文件批量转xlsx
# 作者:      Jas
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# 调用模块
import dbfread
import subprocess as sub
import pandas as pd
import os
# 定义
def clear():
    """清屏"""
    sub.call('cls', shell=True)
def main():
    """主模块，用于转换dbf文件"""
    # 声明
    cnt_errors = 0
    # 获取需转换的dbf路径
    script_path = os.path.dirname("<文件路径>")
    # 清屏
    clear()
    # 寻找dbf文件
    print('你家主子正在寻找dbf猫粮.')
    # 匹配dbf文件
    for dirpath, dirname, filenames in os.walk(script_path):
        for filename in filenames:
            if filename.endswith(".dbf"):
                print("Convert: {filename} to .xlsx".format(filename=filename))
                # 合并文件路径
                full_path = dirpath + "\\" + filename
                # 载入dbf文件，encoding根据需要更改
                try:
                    table = dbfread.DBF(full_path, encoding="gbk", ignore_missing_memofile=False)
                except dbfread.exceptions.DBFNotFound as dbf_exc:
                    print("Error occurred: \n{file} \n{error}".format(file=filename, error=dbf_exc))
                    cnt_errors += 1
                    continue
                # 读取数据载入DataFrame
                df = pd.DataFrame(iter(table),dtype=str)
                # 去除最后四个字符
                xlsx_file = filename[:-4] + ".xlsx"
                # 保存路径
                output_path_xlsx = os.path.join(script_path, xlsx_file)
                # 打印出信息.
                print("Convert: {filename} to .xlsx".format(filename=filename))
                df.to_excel(output_path_xlsx, index=None)
                print("******ojbk******")
    # 打印出未转换的文件数量
    if cnt_errors > 0:
        print('Amount of not converted files: {}'.format(cnt_errors))
# 程序入口
if __name__ == '__main__':
    main()