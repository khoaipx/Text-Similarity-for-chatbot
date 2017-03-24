#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import sys
import codecs


def get_info(collection):
    infos = list()
    can_get = False
    for line in collection:
        if line.startswith('Decode:'):
            can_get = True
        elif line.startswith('Text:'):
            can_get = False
        if can_get:
            infos.append(line)
    return ' '.join(infos)


def get_messages(raw_data_dir):
    messages = list()
    for root, dirs, files in os.walk(raw_data_dir):
        for f in files:
            # if f == 'dialogs.tsv':
            if f == 'chatbot.log':
                path = os.path.join(root, f)
                temp = list()
                for line in codecs.open(path, 'r', 'utf8'):
                    line = line.replace('\n', '')
                    if line.startswith('----------------Handler'):
                        message = get_info(temp)
                        if message != '':
                            messages.append(message)
                        temp = list()
                    else:
                        temp.append(line)
                message = get_info(temp)
                if message != '':
                    messages.append(message)
    writer = codecs.open('chat.txt', 'w', 'utf8')
    for message in messages:
        writer.write(message[len('Decode: '):] + '\t1\n')
    writer.close()


def find_message(raw_data_dir, mess):
    for root, dirs, files in os.walk(raw_data_dir):
        for f in files:
            # if f == 'dialogs.tsv':
            if f == 'chatbot.log':
                path = os.path.join(root, f)
                temp = list()
                for line in codecs.open(path, 'r', 'utf8'):
                    line = line.replace('\n', '')
                    if line.startswith('----------------Handler'):
                        message = get_info(temp)
                        if message.find(mess) != -1:
                            print path
                            print temp[0]
                            print temp[1]
                            print temp[2]
                        temp = list()
                    else:
                        temp.append(line)
                message = get_info(temp)
                if message.find(mess) != -1:
                    print path
                    print temp[0]
                    print temp[1]
                    print temp[2]


def main():
    current_dir = os.curdir
    # get_messages(current_dir)
    message = u'Xin lỗi, Bạn nhập sai định dạng cho ngày tháng khởi hành (26:3), mời bạn nhập lại theo các định dạng sau'
    find_message(current_dir, message)


if __name__ == '__main__':
    main()
