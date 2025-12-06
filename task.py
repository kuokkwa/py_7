class Node:
    """ Клас, що реалізує вузол дерева """
    def __init__(self, key):
        """ Конструктор - створює вузол дерева
        :param key: ключ вузла, що створюється
        """
        self.mKey = key
    def setKey(self, key):
        """ Встановлює ключ для вузла
        :param key: нове значення ключа
        """
        self.mKey = key
    def key(self):
        """ Повертає ключ вузла
        :return: ключ вузла
        """
        return self.mKey
    def __str__(self):
        """ Повертає ключ вузла.
        :return: рядок, у вигляді "key"
        """
        return str(self.mKey)

class Tree(Node):
    """ Клас, що реалізує структуру даних дерево """
    def __init__(self, key):
        """ Конструктор - створює вузол дерева
        :param key: ключ вузла, що створюється
        """
        super().__init__(key)
        self.mChildren = []

    def addChild(self, child):
        """ Додає до поточного вузла заданий вузол (разом з відповідним піддеревом) """
        self.mChildren.append(child)

    def removeChild(self, key):
        """ Видаляє у поточному вузлі вузол-дитину за ключем """
        for child in self.mChildren:
            if child.key() == key:
                self.mChildren.remove(child)
                return True
        return False

    def getChild(self, key):
        """ За заданим ключем, повертає вузол зі списку дітей """
        for child in self.mChildren:
            if child.key() == key:
                return child
        return None

    def getChildren(self):
        """ Повертає список дітей поточного вузла """
        return self.mChildren

# Дерево, варіант 10
def createVariantTree():

    # Листя
    node3 = Tree(3)
    node13 = Tree(13)
    node17 = Tree(17)

    # Внутрішні вузли
    node2 = Tree(2)
    node2.addChild(node3)
    node4 = Tree(4)
    node4.addChild(node2)
    node18 = Tree(18)
    node18.addChild(node17)
    node16 = Tree(16)
    node16.addChild(node13)
    node16.addChild(node18)

    # Корінь
    root = Tree(10)
    root.addChild(node4)    # 10 -> 4
    root.addChild(node16)   # 10 -> 16

    return root

# Обходи
def dfs_preorder(node, result=None):
    """ Рекурсивний обхід в глибину (pre-order) """
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.key())
    for child in node.getChildren():
        dfs_preorder(child, result)
    return result

from collections import deque
def bfs_level_order(root):
    """ Обхід в ширину (level-order / BFS) """
    if root is None:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node.key())
        for child in node.getChildren():
            q.append(child)
    return result

# Головна програма
if __name__ == "__main__":
    tree = createVariantTree()

    dfs_order = dfs_preorder(tree)
    bfs_order = bfs_level_order(tree)

    print("Обхід в глибину:", dfs_order)
    print("Обхід в ширину:", bfs_order)