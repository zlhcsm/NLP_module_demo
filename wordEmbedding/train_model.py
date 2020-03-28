# -*- coding: utf-8 -*-

# @Time  : 2020-03-24 20:02

# @Author : 张磊

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

# @Project : wordEmbedding

# @FileName: train_model.py

# @Software: PyCharm

# @  Blog:https://blog.csdn.net/zzzzlei123123123

import logging
import os
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences


def train_model():
    # 日志信息输出
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    # check and process input arguments
    # if len(sys.argv) < 4:
    #     print(globals()['__doc__'] % locals())
    #     sys.exit(1)
    # input_dir, outp1, outp2 = sys.argv[1:4]
    # input为输入语料， outp1为输出模型， outp2位vector格式的模型
    input_dir = 'data/douluo_cut_word.txt'
    outp1 = 'model/douluo.model'
    outp2 = 'model/douluo.vector'
    # 训练模型
    # 输入语料目录:PathLineSentences(input_dir)
    # embedding size:256 共现窗口大小:10 去除出现次数5以下的词,多线程运行,迭代10次
    model = Word2Vec(PathLineSentences(input_dir),
                     size=256, window=10, min_count=5,
                     workers=multiprocessing.cpu_count(), iter=10)
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)
    # 运行命令:输入训练文件目录 python word2vec_model.py data baike.model baike.vector


if __name__ == '__main__':

    train_model()
