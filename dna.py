from node_types import FrozenNode
import immutable_list as il


def convert_to_nodes(string):
    if len(string) <= 0:
        return
    else:
        value = string[0]
        next_1 = convert_to_nodes(string[1:])
        return FrozenNode(value, next_1)


def convert_to_string(dna_seq):
    result = il.to_str(dna_seq.head)
    return result[1:len(result)-2]


def length_rec(dna_seq, count=0):
    if dna_seq.head is None:
        return 0
    else:
        length_rec(dna_seq.next, count+1)
        return count



def is_match(dna_seq1, dna_seq2):
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    elif dna_seq1.value is dna_seq2.value:
        return is_match(dna_seq1.next, dna_seq2.next)
    else:
        return False


def is_pairing(dna_seq1, dna_seq2):
    if length_rec(dna_seq1) == length_rec(dna_seq2):
        return True
    


def substitution(dna_seq, idx, base):
    pass

def insertion(first, second, index):
    if index == 0:
        return il.concatenate(first, second)
    elif first is None:
        raise IndexError("Invalid Insertion Index")
    else:
        return FrozenNode(first.value, insertion(first.next, second.next, index-1))

def deletion(dna_seq, idx, segment_size):
    pass

def duplication(dna_seq, idx, segment_size):
    pass