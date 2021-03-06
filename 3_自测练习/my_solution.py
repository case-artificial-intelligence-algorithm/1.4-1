# 利用哈夫曼编码算法构造表示哈夫曼树
class Node(object):
    # 定义二叉树T中节点的数据结构
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None

class HuffmanTree(object):
    def __init__(self, c):
        # 初始化最小堆优先队列queue
        self.queue = [Node(part[0], part[1]) for part in c]
        # 存放所有编码结果
        self.result=[]
        # 用b记录每个位置的编码
        self.b = list(range(len(c)))
        # 初始化根节点
        self.root = self.queue[0]
        # queue长度不为1时，对队列中的元素执行哈夫曼算法
        while len(self.queue) != 1:
            raise NotImplementedError('请用哈夫曼算法构造哈夫曼树')

    # 编码输出
    def encode(self, tree, length):
        node = tree
        if (not node):
            return
        # 判断是否是叶子节点，如果是叶子节点则输出对应编码
        elif node.name:
            x = str(node.name) + '的编码为:'
            for i in range(length):
                x += str(self.b[i])
            self.result.append(x)
            return
        # 左分支用0编码
        self.b[length] = 0
        # 向左递归
        self.encode(node.left, length + 1)
        # 右分支用1编码
        self.b[length] = 1
        # 向右递归
        self.encode(node.right, length + 1)

    def get_code(self):
        self.encode(self.root, 0)

if __name__ == '__main__':
    pass