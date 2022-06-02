#!/usr/bin/env python3

from my_solution import HuffmanTree


# 测试用例
def test_solution():
    C = [('a', 18), ('b', 9), ('c', 24), ('d', 4), ('e', 30), ('f', 15)]
    # 初始化哈夫曼树
    tree = HuffmanTree(C)
    # 哈夫曼编码
    tree.get_code()
    #获取每个元素的哈夫曼编码
    result=tree.result
    # 正确答案
    correct_solution = ['a的编码为:00',
                        'c的编码为:01',
                        'd的编码为:1000',
                        'b的编码为:1001',
                        'f的编码为:101',
                        'e的编码为:11']


    assert correct_solution == result