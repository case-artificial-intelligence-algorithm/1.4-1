# 利用哈夫曼编码算法构造表示最优前缀码的二叉树T
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
            # 将queue中的元素按节点的权值从大到小的顺序排序
            self.queue.sort(key=lambda node: node.value, reverse=True)
            # 从队列中选取权值最小的两个节点生成一个新节点t
            t = Node(value=(self.queue[-1].value + self.queue[-2].value))
            # t的左孩子是此时queue中权值最小的节点，且将该权值最小的节点从队列中删除
            t.left = self.queue.pop(-1)
            # t的右孩子是此时queue中权值最小的节点，且将该权值最小的节点从队列中删除
            t.right = self.queue.pop(-1)
            # 将新节点t加入到queue中
            self.queue.append(t)
            # root表示哈夫曼树的根节点b
            self.root = self.queue[0]

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
    C = [('a', 18), ('b', 9), ('c', 24), ('d', 4), ('e', 30), ('f', 15)]
    # 初始化哈夫曼树
    tree = HuffmanTree(C)
    # 哈夫曼编码
    tree.get_code()
    # 获取每个元素的哈夫曼编码
    print(tree.result)