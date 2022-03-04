

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
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

    def print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def check_palindrome(self):
        ''' Check if the linkedlist is a palindrome '''

        # Save a copy of reversed list in a list
        list = []
        curr = self.head
        while curr:
            list.append(curr.data)
            curr = curr.next

        sorted_list = list
        reversed_list = list[::-1]

        # Check if equal
        if sorted_list == reversed_list:
            print("The list is a palindrome")
        else:
            print("The list is not a palindrome")


if __name__ == "__main__":

    list = LinkedList()

    list.insert(5)
    list.insert(4)
    list.insert(1)
    list.insert(4)
    list.insert(5)
    list.print()
    list.check_palindrome()
