# -*- coding: utf-8 -*-

# @Time  : 2020-03-24 19:57

# @Author : 张磊

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

# @Project : wordEmbedding

# @FileName: seg_words.py

# @Software: PyCharm

# @  Blog:https://blog.csdn.net/zzzzlei123123123
import jieba


def seg_words():
    # 定义一些常量值，多次调用的文件路径放在这里，容易修改
    origin_file = "data/douluo_utf8.txt"  # 初代文件
    stop_words_file = "data/stop_words.txt"  # 停用词路径
    user_dict_file = "data/user_dict.txt"  # 用户自定义词典路径
    stop_words = list()
    # 加载停用词
    with open(stop_words_file, 'r', encoding="utf8") as stop_words_file_object:
        contents = stop_words_file_object.readlines()
        for line in contents:
            line = line.strip()
            stop_words.append(line)
    # 加载用户字典
    jieba.load_userdict(user_dict_file)
    target_file = open("data/douluo_cut_word.txt", 'w', encoding="utf-8")
    with open(origin_file, 'r', encoding="utf-8") as origin_file_object:
        contents = origin_file_object.readlines()
        for line in contents:
            line = line.strip()
            out_str = ''
            word_list = jieba.cut(line, cut_all=False)
            for word in word_list:
                if word not in stop_words:
                    if word != "\t":
                        out_str += word
                        out_str += ' '
            target_file.write(out_str.rstrip() + "\n")
    target_file.close()
    print("end")


if __name__ == '__main__':
    seg_words()