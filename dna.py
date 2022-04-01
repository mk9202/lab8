from node_types import FrozenNode
from immutable_list import concatenate


def convert_to_nodes(string):
    if len(string) <= 0:
        return
    else:
        value = string[0]
        next = convert_to_nodes(string[1:])
        return FrozenNode(value, next)


def is_match(first, second):
    if first is None and second is None:
        return True
    elif first is None or second is None:
        return False
    elif first.value is second.value:
        return is_match(first.next, second.next)
    else:
        return False


def insertion(first, second, index):
    if index == 0:
        return concatenate(first, second)
    elif first is None:
        raise IndexError("Invalid Insertion Index")
    else:
        return FrozenNode(first.value, insertion(first.next, second.next, index-1))



    
