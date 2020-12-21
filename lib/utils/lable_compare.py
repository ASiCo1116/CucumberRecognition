import os
import sys

from glob import glob

def main(folder):
    print('Start')

    jpg_dic = []
    xml_dic = []

    for name in glob(f'./lib/data/labelled/{folder}/*'):
        file_name = name.split('.')[1]
        if name.endswith('.jpg'):
            if file_name not in jpg_dic:
                jpg_dic.append(file_name)

        if name.endswith('.xml'):
            if file_name not in xml_dic:
                xml_dic.append(file_name)
    a = list(set(xml_dic) - set(jpg_dic))
    print(a)
    print(len(a))
    for file in a:
        to_be_remove = '.' + file.replace('\\', '/') + '.xml'
        print(to_be_remove)
        os.remove(to_be_remove)
    print('Finish')

if __name__ == "__main__":
    main(sys.argv[1])