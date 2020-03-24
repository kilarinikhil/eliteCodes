'''
Simple linked list. 

Available functions
insert(value): inserts a value into linked list
remove(value): remove the first occurence of the value
'''

class node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class linkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def insert(self,value):
        tmpNode = node(value)

        if self._tail == None:
            self._head = self._tail = tmpNode

        else:
            self._tail.next = tmpNode
            self._tail = tmpNode
        self._len += 1

    def __len__(self):
        return (self._len)

    def __iter__(self):
        yield from self._iter(self._head)

    def _iter(self,node):
        if node:
            yield node.value
            yield from self._iter(node.next)

testll = linkedList()

testll.insert(5)
print(list(testll))
print(len(testll))
testll.insert(7)
print(list(testll))
print(len(testll))
