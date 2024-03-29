from LinkedList import LinkedList
from sorting.Criteria import Criteria

class Tuples(Criteria):

    def __init__(self, elements, *args, **kwargs):
        self.elements = elements
        return super().__init__(*args, **kwargs)

    def sort(self, original, asc=True):
        ls = LinkedList()
        dictionary = original.count_elements()
        last = 1 if asc else 0
        first = 0 if asc else 1
        while dictionary[first] > 0 or dictionary[last] > 0:
            value = first if dictionary[first] > 0 else last
            for i in range(self.elements * 2):
                if i == self.elements:
                    value = last if dictionary[last] > 0 else first
                if dictionary[value] > 0:
                    ls.push(value)
                    dictionary[value] -= 1
                else:
                    break
        return ls.head