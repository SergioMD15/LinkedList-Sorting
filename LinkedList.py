class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if not self.next:
            self.next = Node(val)
        else:
            self.next.add(val)

    def remove(self, val):
        if self.next.val == val:
            self.next = self.next.next
        else:
            self.next.remove(val)
    
    def __str__(self):
        return str(self.val)


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
    
    def push(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            self.head.add(val)
        self.length += 1
    
    def add_first(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            aux = Node(val)
            aux.next = self.head
            self.head = aux
        self.length += 1

    def get_length(self):
        return self.length
    
    def remove(self, val):
        if self.head:
            if self.head.val == val:
                self.head = self.head.next
            elif self.head.next.val == val:
                self.head.next = self.head.next.next
            else:
                self.head.remove(val)
            self.length -= 1
    
    def remove_by_index(self, index):
        if self.head:
            aux = self.head
            if index == 0:
                self.head = self.head.next
            else:
                while index > 1 and aux:
                    aux = aux.next
                    index -= 1
                if index <= 1 and aux.next:
                    aux.next = aux.next.next
            self.length -= 1

    def sort(self, criteria, asc=True):
        self.head = criteria.sort(self, asc)

    def count_elements(self):
        aux = self.head
        result = {}
        while aux:
            if aux.val in result.keys():
                result[aux.val] += 1
            else:
                result[aux.val] = 1
            aux = aux.next
        return result

        

    def __str__(self):
        aux = self.head
        result = ''
        if aux:
            result = aux.__str__()
            while aux.next:
                aux = aux.next
                result += ', ' + aux.__str__()
        return result
