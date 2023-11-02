class TrieNode:
    def __init__(self):
        self.children = {}  # дочерние узлы текущего узла TrieNode.
        # Ключи - символы строки. Каждый символ - связка между текущим узлом и следующим узлом.
        self.output = []  # список подстрок, которые заканчиваются в данном узле.
        # используется для хранения всех возможных найденных подстрок.
        self.failure = None  # указывает на узел, в который нужно перейти в случае отсутствия совпадения символа.
        # позволяет сделать переход назад в дереве Trie и продолжить поиск с помощью failure.


def build_bor(substring):
    root = TrieNode()
    node = root  # корень
    for symbol in substring:
        if symbol not in node.children:
            node.children[symbol] = TrieNode()  # Если символа нет в children,
            # То создается новый узел и добавляется в children узла node.
            # В этот новый узел будет переход по символу.
        node = node.children[symbol]  # продолжаем построение дерева.
    node.output.append(substring)
    # Добавление подстроки в output узла node.
    # Нужно для того, чтобы при построении Trie были сохранены все найденные подстроки,
    # которые заканчиваются в данном узле.
    return root


def build_automaton(substring):
    root = build_bor(substring)
    nodes = [node for node in root.children.values()]  # содержит все дочерние узлы корневого узла
    for node in nodes:
        node.failure = root  # присваиваем всем узлам ссылку на корневой узел
    while nodes:
        current_node = nodes[0]
        nodes = nodes[1:]  # Текущий узел извлекается из начала списка и удаляется из него.
        for key, child_node in current_node.children.items():
            nodes.append(child_node)
            failure = current_node.failure  # добавляем дочерний узел текущего узла в список и передаем ссылку
            while failure and key not in failure.children:
                failure = failure.failure
            child_node.failure = failure.children[key] if failure else root
            # связываем текущий узел с узлом, куда нужно перейти при отсутствии совпадения символа.
    return root


def find_substring(string, substring):
    root = build_automaton(substring)
    node = root
    i = 0
    while i < len(string):
        if string[i] in node.children:
            node = node.children[string[i]]  # Проверяем содержится ли символ в дочерних узлах.
            # Если да, то переходим на дочерний узел. Если у него есть значение в output,
            # то подстрока нашлась.
            i = i + 1
            if node.output:
                return True
        else:
            node = node.failure
            if not node:
                node = root
                i = i + 1
    return False
