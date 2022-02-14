
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
        else:
            self.head = newNode

    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def rotateList(self, k):
        ''' Rotate the linked list to the right by k spots '''
        traversed = 1
        curr = self.head
        temp = LinkedList()
        while (traversed < k):
            curr = curr.next
            traversed += 1

        while (curr):
            temp.insert(curr.data)
            curr = curr.next

        curr = self.head
        traversed = 1
        while (traversed <= k - 1):
            temp.insert(curr.data)
            traversed += 1
            curr = curr.next

        temp.printList()


if __name__ == '__main__':
    lst = LinkedList()
    lst.insert(1)
    lst.insert(2)
    lst.insert(3)
    lst.insert(4)
    lst.insert(5)
    # lst.rotateList(3)

    lst2 = LinkedList()
    lst2.insert(7)
    lst2.insert(7)
    lst2.insert(3)
    lst2.insert(5)
    lst2.rotateList(2)
