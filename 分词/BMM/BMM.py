# 使用逆向最大匹配算法实现中文分词
words_dic = []

def init():
    """
    读取词典文件
    :return:
    """
    with open("../dic/dict.txt", "r", encoding="utf8") as dic_input:
        for word in dic_input:
            words_dic.append(word.split(" ")[0].strip())


# 实现逆向最大匹配算法中的切词方法
def cut_words(raw_sentence, words_dic):
    # 统计词典中词的最长长度
    max_length = max(len(word) for word in words_dic)
    sentence = raw_sentence.strip()
    # 统计序列长度
    words_length = len(sentence)
    # 存储切分出来的词语
    cut_word_list = []
    # 判断是否需要继续访问
    while words_length > 0:
        max_cut_length = min(max_length, words_length)
        sub_sen = sentence[-max_cut_length:]
        while max_cut_length > 0:
            if sub_sen in words_dic:
                cut_word_list.append(sub_sen)
                break
            elif max_cut_length == 1:
                cut_word_list.append(sub_sen)
                break
            else:
                max_cut_length = max_cut_length - 1
                sub_sen = sub_sen[-max_cut_length:]
        sentence = sentence[0:-max_cut_length]
        words_length = words_length - max_cut_length
    cut_word_list.reverse()
    words = "/".join(cut_word_list)
    return words

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
