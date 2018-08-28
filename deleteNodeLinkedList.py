'''
This program deletes a node in the linked list.
@author: Asif Nashiry
'''

# Node class defines a Node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        # number of elements in a list
        self.counter = 0

# insert nodes at the end of a list
    def insertNode(self, data):
        # create a new node
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = newNode
        self.counter += 1

# count the number of elements in the list
    def numberOfNode(self):
        return self.counter

# print the list
    def printList(self):
        if self.head is None:
            return
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, ' ', end=" ")
            currentNode = currentNode.next

# find the location of the node to be deleted
    def findLocTarget(self, target):
        if self.head == None:
            print('The list is empty')
            return None
        currentNode = self.head
        while currentNode is not None:
            if target == currentNode.data:
                return currentNode
            currentNode = currentNode.next
        return None

# delete the node
    def deleteNode(self, targetLoc):
        if targetLoc is None:
            print('The data is not in the list')
            return
        elif targetLoc == self.head:
            currentNode = self.head
            self.head = currentNode.next
            del currentNode
        else:
            currentNode = self.head
            prevNode = self.head
            while currentNode != targetLoc:
                prevNode = currentNode
                currentNode = currentNode.next
            prevNode.next = currentNode.next
            del currentNode
        self.counter -= 1


