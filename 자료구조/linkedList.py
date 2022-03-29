class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def find(self, value):
        curr_node = self.head
        while curr_node.value != value:
            curr_node = curr_node.next

        return curr_node

    def append(self, new_value):
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # 파라미터로 받은 노드 다음에 끼워 넣기
    def insert(self, node, new_value):
        new_node = Node(new_value)
        new_node.next = node.next
        node.next = new_node

    def remove(self, value):
        prev_node = self.head
        while prev_node.next.value != value:
            prev_node = prev_node.next

        if prev_node is not None:
            prev_node.next = prev_node.next.next

    def display(self):
        curr_node = self.head
        display_string = "["
        while curr_node is not None:
            display_string += f"{curr_node.value}, "
            curr_node = curr_node.next

        display_string = display_string[0:len(display_string) - 2]
        display_string += "]"
        print(display_string)


linkedList = SinglyLinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(5)
linkedList.display()
print(linkedList.find(3))
linkedList.remove(3)
linkedList.display()
linkedList.insert(linkedList.find(2),10)
linkedList.display()



