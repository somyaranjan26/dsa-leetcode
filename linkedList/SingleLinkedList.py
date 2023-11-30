class Node:
    def __init__(self, data):
        self.data = data
        self.nextPtr = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    
    def insertAtBeginning(self, data):
        newNode = Node(data)
        
        newNode.nextPtr = self.head
        self.head = newNode
    
    def insertAtEnd(self, data):
        newData = Node(data)
        
        temp = self.head
        
        if self.head is None:
            self.head = newData
        else:
            temp = self.head
            
            while temp.nextPtr:
                temp = temp.nextPtr
            
            temp.nextPtr = newData
        
    def insertAfterNode(self, prevNode, data):
        newData = Node(data)
        
        temp = self.head
        
        while temp:
            if temp.data == prevNode:
                newData.nextPtr = temp.nextPtr
                temp.nextPtr = newData
                break
            else:
                temp = temp.nextPtr
                
                
    def deleteNode(self, pos):
        temp = self.head
        
        for _ in range(pos - 1):
            temp = temp.nextPtr
            if temp is None:
                return
            
        tempPtr = temp.nextPtr.nextPtr
        temp.nextPtr = None
        temp.nextPtr = tempPtr
        
    def countNode(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.nextPtr

        return count
    
    def searchNode(self, data):
        temp = self.head
        pos = -1
        while temp:
            if temp.data == data:
                pos += 1
                return pos, True
            else:
                temp = temp.nextPtr

        return pos, False 
    
    def mergeLists(self, head1, head2):
        newList = None
        
        if head1 is None:
            return head2
        
        if head2 is None:
            return head1
        
        if head1.data <= head2.data:
            newList = head1
            newList.nextPtr = self.mergeLists(head1.nextPtr, head2)
        else:
            newList = head2
            newList.nextPtr = self.mergeLists(head1, head2.nextPtr)
        
        return newList
          
            
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" ", end=' ')
            temp = temp.nextPtr
            
llist = LinkedList()

llist.insertAtBeginning(30)
llist.insertAtBeginning(20)
llist.insertAtBeginning(10)
llist.insertAtEnd(40)
# llist.insertAfterNode(30, 25)
llist.printLinkedList()

print()
print(llist.countNode())

llist.deleteNode(2)
print()
llist.printLinkedList()

print()
print(llist.countNode())

print()
pos, res = llist.searchNode(20)
print(res, " At ", pos+1)

llist2 = LinkedList()
llist2.insertAtEnd(11)
llist2.insertAtEnd(24)
llist2.insertAtEnd(45)
llist2.insertAtEnd(64)

print()
llist2.printLinkedList()

llist3 = LinkedList()
llist3.head = llist3.mergeLists(llist.head, llist2.head)

print()
llist3.printLinkedList()