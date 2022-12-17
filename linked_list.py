class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def insertStart(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
            self.next = None
        else:
            node = Node(data)
            node.next = self.head
            self.head = node

    def insertEnd(self, data):
        if self.head == None:
            node = Node(data)
            node.next = None
            self.head = node
        else:
            startNode = self.head
            while True:
                if startNode.next == None:
                    node = Node(data)
                    node.next = None
                    startNode.next = node
                    break
                else:
                    startNode = startNode.next
    def insertMiddle(self, findData, insertingData):
        startNode = self.head
        while True:
            if startNode.data == findData:
                newNode = Node(insertingData)
                newNode.next = startNode.next
                startNode.next = newNode
                break
            else:
                startNode = startNode.next
    def deleteEnd(self):
        startNode = self.head
        while True:
            if startNode.next == None:
                self.head = None
                break
            elif startNode.next.next == None:
                startNode.next = None
                break
            else:
                startNode = startNode.next
    def deleteStart(self):
        node = self.head.next
        if node != None:
            self.head = node
            self.next = node.next
        else:
            self.head = node
            self.next = None
    def printAllNodes(self):
        node = self.head
        while True:
            if node == None:
                break
            print(node.data)
            node = node.next



linked_list = LinkedList()


linked_list.printAllNodes()