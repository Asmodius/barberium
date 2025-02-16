import operator

class TreeStore:
    def __init__(self, items):
        self.items = items
        self.item_by_id = {item['id']: i for i, item in enumerate(items)}
        # {'root': [1, 2, 3, 4, 5, 6, 7, 8],
        # 1: [2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 7, 8], 2: [4, 5, 6, 7, 8, 7, 8, 7, 8, 7, 8], 4: [7, 8]}

        # 'root': [1]  [2,3],[4,5,6],[7,8],
        # 1: [2, 3], [4,5,6], [7,8]
        # 2: [4, 5, 6], [7,8]
        # 3
        # 4: [7, 8]
        # 5
        # 6
        # 7

        self.item_by_parent = {}
        # self.item_by_children = {}
        for item in items:
            parent = item['parent']
            _id = item['id']
            self.item_by_parent.setdefault(parent, [])
            self.item_by_parent[parent].append(_id)

        for k, v in self.item_by_parent.items():
            print('----------')
            print('R1', k, v)
            x = self._by_parent(k, v)
            print('RE', k, x)
            # print('R1', k, v)
            # for i in v:
            #     print('R2', i)
            #     self._by_parent(i)


    def _by_parent(self, parent, v):
        data = v
        try:
            for _parent in v:
                _v = self.item_by_parent[_parent]
                if _v:
                    data += _v
                    self._by_parent(_parent, _v)
                    # print('R3', parent, i, x)
        except KeyError:
            print('R4', parent)
        # self.item_by_parent[parent] = data
        return data

    #    {"id": 1, "parent": "root"},
    #    {"id": 2, "parent": 1, "type": "test"},
    #    {"id": 3, "parent": 1, "type": "test"},

    #    {"id": 4, "parent": 2, "type": "test"},
    #    {"id": 5, "parent": 2, "type": "test"},
    #    {"id": 6, "parent": 2, "type": "test"},
    #    {"id": 7, "parent": 4, "type": None},
    #    {"id": 8, "parent": 4, "type": None}

    def get_all(self):
        """Возвращает изначальный массив элементов."""
        return self.items

    def get_item(self, _id):
        """Возвращает элемент по id."""
        return self.items[self.item_by_id[_id]]

    def get_children(self, _id):
        """Возвращает массив дочерних элементов."""
        # parent = self.get_item(_id)['id']
        # data = []
        # for i in self.item_by_parent[parent]:
        #     pass

    def get_all_parents(self, item_id):
        """Возвращает массив родительских элементов."""


# Комментарии:
# Имена методов в задании противоречат PEP N802. Я перевел их в нижний регистр.


# Требования: максимальное быстродействие, следовательно, минимальное количество обходов массива при операциях,
# в идеале, прямой доступ к элементам без поиска их в массиве.

items1 = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items1)
print(ts.item_by_parent)

# Примеры использования:
#  - ts.getAll() // [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},{"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},{"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#
#  - ts.getItem(7) // {"id":7,"parent":4,"type":None}
# print(ts.get_item(7))

#  - ts.getChildren(4) // [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#  - ts.getChildren(5) // []
#
#  - ts.getAllParents(7) // [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]

for k, v in zip(['p3', 'p2', 'p1', 'n0', 'n1', 'n2', 'n3'], [11,12,1, 2, 3,4,5]):
    print('ll', k, v)