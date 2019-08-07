from LinkedList import LinkedList

class Criteria:

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    ## DEFAULT BEHAVIOR ##
    def sort(self, original, asc=True):
        ls = LinkedList()
        root = original.head
        last = 1 if asc else 0
        first = 0 if asc else 1
        while root:
            if root.val == last:
                ls.push(last)
            else:
                ls.add_first(first)
            root = root.next
        return ls.head