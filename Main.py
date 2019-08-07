import math
import random
from LinkedList import LinkedList
from sorting.Criteria import Criteria
from sorting.Tuples import Tuples

def generate_array(size):
    result = LinkedList()
    for i in range(size):
        result.push(int(random.randint(0,1)))
    return result

l = generate_array(10)

print(l)

l.sort(Tuples(5))

print(l)