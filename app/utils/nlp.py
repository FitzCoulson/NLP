import jieba


# 获取停用词列表
def get_stopword_list(file):
    with open(file, 'r', encoding='utf-8') as f:
        stopword_list = [word.strip('\n') for word in f.readlines()]
    return stopword_list

def clean_stopword(text):
    seg_list=segment(text)
    stopword_file = 'C:/Users/Administrator/Desktop/NLP/app/utils/hit_stopwords.txt'
    stopword_list = get_stopword_list(stopword_file)
    word_list=[]
    for w in seg_list:
        if w not in stopword_list:
            word_list.append(w)
    return word_list

# 去除停用词
def print_clean_stopword(text):
    seg_list = jieba.lcut(text)
    stopword_file = 'C:/Users/Administrator/Desktop/NLP/app/utils/hit_stopwords.txt'
    stopword_list = get_stopword_list(stopword_file)
    result = ''
    for w in seg_list:
        if w not in stopword_list:
            result += w
    return result


# 分词
def segment(text):
    seg_list = jieba.lcut(text)
    return seg_list


def printsegment(text):
    seg_list = segment(text)
    seg_text = ''
    for w in seg_list:
        seg_text += w + ' || '
    seg_text = seg_text[0:-4]
    return seg_text


# 高频词提取
def high_freq(word_list, topk=5):
    tf_dic = {}
    for w in word_list:
        tf_dic[w] = tf_dic.get(w, 0) + 1
    return sorted(tf_dic.items(), key=lambda x: x[1], reverse=True)[:topk]

def print_high_freq(text):
    dict=high_freq(clean_stopword(text))
    high_freq_words=''
    for w,v in dict:
        high_freq_words+=f'{w}:{v}\n'
    return high_freq_words,dict


# 调用函数
def nlp(text):
    seg_list = segment(text)
    result, word_list = clean_stopword(seg_list)
    hf_word = high_freq(word_list)
    return seg_list, result, hf_word
