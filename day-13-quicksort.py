import copy


f = open("./inputs/day-13-input.txt")
input = [line.strip() for line in f]

def make_proper_packets(fifo: list) -> list:
    '''Converts a packet from a list of strings into a proper packet with integers and nested lists.'''
    res = []
    tmp_int = ""
    while True:
        c = fifo.pop(0)
        if c == "[":
            # recursive calls access the same list via reference:
            res.append(make_proper_packets(fifo))
        elif c == ",":
            if tmp_int:
                res.append(int(tmp_int))
                tmp_int = ""
        elif c == "]":
            if tmp_int:
                res.append(int(tmp_int))
            return res
        else:
            tmp_int += c

def check_packet_order(left: list, right: list) -> int:
    '''Return 1 for in order, 0 for out of order, -1 for no decision.'''
    # Deepcopy inputs so list popping doesn't have an effect outside of this function:
    left_copy = copy.deepcopy(left)
    right_copy = copy.deepcopy(right)
    while left_copy and right_copy:
        l = left_copy.pop(0)
        r = right_copy.pop(0)
        if type(l) is not type(r) :
            if type(l) is int:
                l = list([l])
            else:
                r = list([r])
        if type(l) is int and type(r) is int:
            if l < r:
                return 1
            elif l > r:
                return 0
            else:
                continue
        elif type(l) is list and type(r) is list:
            tmp_res = check_packet_order(l, r)
            if tmp_res != -1:
                return tmp_res
    # one or both lists ran out of items:
    if not left_copy and right_copy:
        return 1
    elif left_copy and not right_copy:
        return 0
    else:
        return -1

def print_packets(packets: list):
    for i, p in enumerate(packets):
        print(f"Packet {i+1}: {p}")
    
def quick_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2]
        left = [x for x in array if check_packet_order(x, pivot) == 1]
        middle = [x for x in array if check_packet_order(x, pivot) == -1]
        right = [x for x in array if check_packet_order(x, pivot) == 0]
        return quick_sort(left) + middle + quick_sort(right)
    
def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    else:
        mid_point = len(array) // 2
        left = merge_sort(array[:mid_point])
        right = merge_sort(array[mid_point:])
    return merge(left, right)

def merge(left: list, right: list) -> list:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if check_packet_order(left, right) == 1:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

sum_inorder_IDs = 0
divider_packets = [[[2]], [[6]]]
unsorted_packets = copy.deepcopy(divider_packets)

for i in range(0, len(input), 3):
    id = i // 3 + 1
    left = list(input[i][1:])
    right = list(input[i + 1][1:])
    left = make_proper_packets(left)
    right = make_proper_packets(right)
    unsorted_packets.extend([copy.deepcopy(x) for x in [left, right]])
    sum_inorder_IDs += id if check_packet_order(left, right) == 1 else 0
    
sorted_packets = quick_sort(unsorted_packets) # faster than merge sort
divider_indices = [sorted_packets.index(x) + 1 for x in sorted_packets if x in divider_packets]
decoder_key = divider_indices[0] * divider_indices[1]

print(f"Sum of in-order packet pair IDs: {sum_inorder_IDs}")
print(f"Decoder key: {decoder_key}")