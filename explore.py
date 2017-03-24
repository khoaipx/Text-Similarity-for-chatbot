import codecs
from collections import Counter
import random


def valid_word(word):
    for c in word:
        if not c.isdigit() and c not in '/\.,h=\':-?()':
            return True
    return False


def clean(token):
    diaratic = '.,?!'
    for c in diaratic:
        token = token.replace(c, '')
    return token


def get_dic():
    vec_file = '/home/khoaipx/Downloads/viwiki/wiki.vi.vec'
    reader = codecs.open(vec_file, 'r', 'utf8')
    reader.readline()
    words = list()
    for line in reader.readlines():
        line = line.strip()
        word = line.split()[0]
        words.append(word)
    writer = codecs.open('dic.txt', 'w', 'utf8')
    for word in words:
        writer.write(word + '\n')
    writer.close()


def test(data_file):
    vec_file = 'dic.txt'
    reader = codecs.open(vec_file, 'r', 'utf8')
    words = list()
    for line in reader.readlines():
        line = line.strip()
        words.append(line)

    nwil = list()
    dic = set()
    for line in codecs.open(data_file, 'r', 'utf8'):
        line = line.replace('\n', '')
        (message, flag) = line.split('\t')
        nwil.append(len(message.split(' ')))
        # dic |= set(message.split(' '))
        for token in message.split(' '):
            token = clean(token)
            if token != '':
                dic.add(token)
        # if len(message.split(' ')) == 1:
        #     print message
    # c = Counter(nwil)
    # total = sum([c[sl] for sl in c])
    # cum = 0.0
    # for sl in c:
    #     cum += float(c[sl])/total
    #     print sl, ': ', c[sl], ' -> ', float(c[sl])/total, ' = ', cum, ' - ', 1.0-cum
    # print 'total: ', sum(c[sl]*sl for sl in c)

    cnt = 0
    for word in dic:
        if word.lower() not in words:
            print word
            cnt += 1
    print 'size: ', len(dic) - cnt


def make_csv(data_file):
    messages = list()
    for line in codecs.open(data_file, 'r', 'utf8'):
        line = line.strip()
        messages.append(line)
    random.shuffle(messages)
    train_size = len(messages)/5 * 4
    train_writer = codecs.open('train.csv', 'w', 'utf8')
    test_writer = codecs.open('test.csv', 'w', 'utf8')
    for line in messages[:train_size]:
        (message, lable) = line.split('\t')
        train_writer.write('"' + lable + '","' + message + '"\n')
    train_writer.close()
    for line in messages[train_size:]:
        (message, lable) = line.split('\t')
        test_writer.write('"' + lable + '","' + message + '"\n')
    test_writer.close()


def main():
    data_file = 'chat.txt'
    # test(data_file)
    # get_dic()
    make_csv(data_file)


if __name__ == '__main__':
    main()
