import BMM
import FMM

# 使用双向最大匹配算法实现中文分词
words_dic = []

def init():
    """
    读取词典文件
    :return:
    """
    with open("../dic/dict.txt", "r", encoding="utf8") as dic_input:
        for word in dic_input:
            words_dic.append(word.split(" ")[0].strip())


# 实现双向最大匹配算法中的切词方法
def cut_words(raw_sentence, words_dic):
    # 后向分词结果
    bmm_words_list = BMM.cut_words(raw_sentence, words_dic)
    # 前向分词结果
    fmm_words_list = FMM.cut_words(raw_sentence, words_dic)
    bmm_words_list_size = len(bmm_words_list)
    fmm_words_list_size = len(fmm_words_list)

    if bmm_words_list_size != fmm_words_list_size:
        if bmm_words_list_size < fmm_words_list_size:
            return bmm_words_list
        else:
            return fmm_words_list
    else:
        FSingle = 0
        BSingle = 0
        isSame = True
        for i in range(len(fmm_words_list)):
            if fmm_words_list[i] not in bmm_words_list:
                isSame = False
            if len(fmm_words_list[i]) == 1:
                FSingle = FSingle + 1
            if len(bmm_words_list[i]) == 1:
                BSingle = BSingle + 1
        if isSame:
            return fmm_words_list
        elif BSingle > FSingle:
            return fmm_words_list
        else:
            return bmm_words_list

def main():
    """
    与用户交互接口
    :return:
    """
    init()
    while True:
        print("请输入您要分词的序列：")
        input_str = input()
        if not input_str:
            break
        result = cut_words(input_str, words_dic)
        print("分词结果")
        print(result)


if __name__ == '__main__':
    main()
