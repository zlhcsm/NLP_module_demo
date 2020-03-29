# -*- coding: utf-8 -*-

# @Time  : 2020-03-24 19:45

# @Author : 张磊

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

# @Project : wordEmbedding

# @FileName: gbk2utf8.py

# @Software: PyCharm

# @  Blog:https://blog.csdn.net/zzzzlei123123123
# -*- coding: utf-8 -*-
def gbk2utf8():
    file_out = open('data/douluo_utf8.txt', 'w', encoding="utf-8")       # 输出文件路径
    with open('data/douluo.txt', 'r', encoding="GB18030") as file_object:
        for line in file_object:
            line = line.strip()
            file_out.write(line + "\n")
    file_out.close()
    print("end")
