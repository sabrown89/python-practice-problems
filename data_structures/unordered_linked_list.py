class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class UnorderedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp


    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            current = current.next
        return False


uol = UnorderedList()

uol.add(31)
uol.add(77)
uol.add(71)
uol.add(93)
uol.add(26)
uol.add(54)

print(uol.size())
print(uol.search(93))
