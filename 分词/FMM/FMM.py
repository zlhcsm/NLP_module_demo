# 使用正向最大匹配算法实现中文分词
words_dic = []


def init():
    """
    读取字典文件
    载入词典
    :return:
    """
    with open("../dic/dict.txt", "r", encoding="utf8") as dict_input:
        for word in dict_input:
            # 文件格式为：单词 词频 词性
            words_dic.append(word.split(" ")[0].strip())


# 实现正向匹配算法中的切词方法
def cut_words(raw_sentence, word_dic):
    # 统计词典中最长的词
    max_length = max(len(word) for word in word_dic)
    sentence = raw_sentence.strip()
    # 统计序列长度
    word_length = len(sentence)
    # 存储切分好的词语
    cut_word_list = []
    while word_length >0:
        max_cut_length = min(max_length, word_length)
        sub_sen = sentence[0:max_cut_length]
        while max_cut_length > 0:
            if sub_sen in word_dic:
                cut_word_list.append(sub_sen)
                break
            elif max_cut_length == 1:
                cut_word_list.append(sub_sen)
                break
            else:
                max_cut_length = max_cut_length - 1
                sub_sen = sub_sen[0:max_cut_length]
        sentence = sentence[max_cut_length:]
        word_length = word_length - max_cut_length
    words = '/'.join(cut_word_list)
    return words


def main():
    init()
    while True:
        print("请输入您要分词的序列")
        input_str = input()
        if not input_str:
            break
        result = cut_words(input_str, words_dic)
        print("分词结果")
        print(result)


if __name__ == '__main__':
    main()
