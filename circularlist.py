
class Node(object):
    """Encapsulation of a singly linked Node to be used in Linked List"""
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.next=nextNode
        
    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

    def __str__(self):
        return "Node data:%s" % (self.data,)



class CircularLinkedList(object):
    """A singly linked circular list. This implementation utilizes a
       sentinel (head) node with None data. This list allows duplicates"""

    def __init__(self):
        self.head = Node(None,None)
        self.head.next = self.head

    def __str__(self):
        retVal = "CircularLinkedList of size = " + str(len(self)) +"\n"
        temp = self.head.next
        while temp is not self.head:
            retVal += temp.__str__() + "\n"
            temp = temp.next
        return retVal


    def __len__(self):
        size = 0
        temp = self.head.next
        while temp is not self.head:
            size += 1
            temp = temp.next
        return size


    def isEmpty(self):
        return len(self) == 0


    def prepend(self, data):
        self.head.next = Node(data, self.head.next)


    def append(self, data):
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
        temp.next = Node(data, self.head)


    def __contains__(self, data):
        temp = self.head.next
        while temp is not self.head:
            if temp.getData() == data:
                return True
            temp = temp.next
        return False


    def removeFirst(self):
        temp = self.head.next
        self.head.next = temp.next
        return temp.getData()


    def removeLast(self):
        trailing, leading = self.head, self.head.next
        while True:
            if leading.next == self.head:
                trailing.next = self.head
                break
            trailing = leading
            leading = leading.next
        return leading.getData()
            
    
    def remove(self, data):
        trailing, leading = self.head, self.head.next
        while leading is not self.head:
            if leading.getData() == data:
                trailing.next = leading.next
                break
            trailing =  leading
            leading = leading.next
        return leading.getData()


    def removeDuplicates(self):
        visited = set()
        trailing = leading = self.head.next
        while leading is not self.head:
            if leading.getData() in visited:
                leading = leading.next
                while leading in visited and leading is not self.head:
                    leading = leading.next
                trailing.next = leading
            else:
                visited.add(leading.getData())
                trailing = leading
                leading = leading.next
                
                


