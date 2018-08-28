'''
This program deletes a node in the linked list.
@author: Asif Nashiry
'''

from deleteNodeLinkedList import LinkedList
import random

# number of elements in the list
numOfData = 15
aList = LinkedList()

# create a list with random numbers
for i in range(numOfData):
    data = random.randint(1, 30)
    aList.insertNode(data)

print('List: ')
aList.printList()
print('\nNumber of elements: ', aList.numberOfNode())

target = int(input('\nEnter the data to be deleted: '))
# find the location of the node to be deleted
targetLoc = aList.findLocTarget(target)

if targetLoc is None:
    print('The element', target, 'does not appear in the list')
else:
    aList.deleteNode(targetLoc)
    print('List after deleting: ')
    aList.printList()
    print('\nNumber of elements: ', aList.numberOfNode())