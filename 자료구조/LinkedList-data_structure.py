class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next

class LinkedList:

    def __init__(self):
        new_node = Node(None,None)
        self.head = new_node
        self.tail = new_node
        self.size = 0

    def clear(self):
        self.head.next = None
        self.tail = self.head
        self.size = 0

    def insert(self, pos, item):
        curr = self.head
        for i in range(pos):
            curr = curr.next
        new_node = Node(item, curr.next)
        curr.next = new_node

        if curr == self.tail:
            self.tail = curr.next

        self.size += 1


    def append(self, item):
        new_node = Node(item,None)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def update(self, pos, item):
        curr = self.head
        for i in range(pos):
            curr = curr.next
        curr.next.item = item

    def getValue(self, pos):
        curr = self.head
        for i in range(pos):
            curr = curr.next

        return curr.next.item

    def remove(self, pos):
        curr = self.head
        for i in range(pos):
            curr = curr.next

        remove_item = curr.next.item
        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next
        self.size -= 1

        return remove_item

    def length(self):
        return self.size

    def print(self):
        curr = self.head
        display_string = "["
        for i in range(self.size):
            display_string += f"{curr.next.item}, "
            curr = curr.next

        display_string = display_string[0:len(display_string) - 2]
        display_string += "]"
        print(display_string)


a = LinkedList()
a.append(4)
a.append(5)
a.append(3)
a.append(10)
a.insert(0,101)
a.print()

a.remove(3)
a.print()

print(a.length())
a.update(0,1)
a.print()