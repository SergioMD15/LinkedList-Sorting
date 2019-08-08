from LinkedList import LinkedList
from sorting.Criteria import Criteria

class Centering(Criteria):

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def sort(self, original, asc=True):
        ls = LinkedList()
        dictionary = original.count_elements()
        last = 1 if asc else 0
        first = 0 if asc else 1
        push = True
        while dictionary[first] > 0 or dictionary[last] > 0:
            value = first if dictionary[first] > 0 else last
            for i in range(original.length):
                if dictionary[first] == 0 and dictionary[last] > 0:
                    value = last
                if push:
                    ls.push(value)
                    push = False
                else:
                    ls.add_first(value)
                    push = True
                dictionary[value] -= 1
        return ls.head