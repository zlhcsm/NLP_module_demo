import gbk2utf8 as gu
import train_model as tm
import seg_words as sm

if __name__ == '__main__':
    # 将文件格式转换为utf8
    # gu.gbk2utf8()

    # 分词
    sm.seg_words()

    # 训练模型
    #tm.train_model()
