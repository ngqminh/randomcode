# random list manipulation things
def list_manip():
    stuff = [1, "a", "b", 2, 3, "c"]
    stuff[:] = [i for i in stuff if not type(i) == int]
    print(stuff)

    stuff = ["1", "2", "A", "B"]
    stuff[:] = [i for i in stuff if not i.isdigit()]
    print(stuff)

    stuff = [1, 2, 3, 4, 5, 6]
    stuff[:] = [i for i in stuff[::-1] if not i%2]
    print(stuff)

# get combinations of items in a list
def combinations():
    ret = []
    stuff = ["a", "b", "c", "d"]
    for i in range(2**len(stuff)):
        idx = bin(i)[2:]
        while(len(idx) < len(stuff)):
            idx = "0" + idx
        interm = []
        for j in range(len(idx)):
            if idx[j] != "0":
                interm.append(stuff[j])
        ret.append(interm)
    print(ret)

# binary search tree
class Node:
    def __init__(self, value, parent):
        self.val = value
        self.parent = parent
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, val):
        inserted = False
        cur = self.root
        while(not inserted):
            if(val < cur.val):
                if(cur.left == None):
                    cur.left = Node(val, cur)
                    inserted = True
                else:
                    cur = cur.left
            else:
                if(cur.right == None):
                    cur.right = Node(val, cur)
                    inserted = True
                else:
                    cur = cur.right

# get the right neighbor of a node
# arthur got asked this question at tripadvisor
# can also be easily modified to do level-order traversal of a binary tree
def right_neighbor(root, q, node):
    if root.val == "Guard":
        if q:
            q.append(root)
            root = q.pop(0)
        else:
            print()
            return

    if root.left:
        q.append(root.left)
    if root.right:
        q.append(root.right)
    # print(root.val, end=' ')
    # code for finding a neighbor
    if root.val == node:
        if q:
            next = q.pop(0)
            if next.val != "Guard":
                return next.val
            else: return -1
        else: return -1

    return right_neighbor(q.pop(0), q, node)

# tree things I guess
def tree_shit():
    node1 = Node(12, None)
    node2 = Node(8, node1)
    node1.left = node2
    tree = BST(node1)
    tree.insert(11)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    q = []
    q.append(Node("Guard", None))
    neighbor = (right_neighbor(node1, q, 1))
    print(neighbor)

# sum of BST nodes
def sum_BST(root):
    if not root:
        return 0
    else:
        return root.val + sum_BST(root.left) + sum_BST(root.right)

# order traversals
def pre_order(node):
    print(node.val)
    if node.left != None:
        pre_order(node.left)
    if node.right != None:
        pre_order(node.right)

def in_order(node):
    if node.left != None:
        in_order(node.left)
    print(node.val)
    if node.right != None:
        in_order(node.right)

def post_order(node):
    if node.left != None:
        post_order(node.left)
    if node.right != None:
        post_order(node.right)
    print(node.val)

# subtract strings... intersect is the same index
def minus_intersect():
    a = "aabbcc"
    b = "ccbbaa"
    ret = [i[0] for i in zip(a,b) if i[0] != i[1]]

    str_ret = ""
    for i in ret:
        str_ret += i

    print(str_ret)

# binary search in an array
def binsearch_array(number, array, start, end):
    idx = (start+end)/2
    if start == end:
        return -1
    if number == array[idx]:
        return idx
    elif number < array[idx]:
        return binsearch_array(number, array, start, idx)
    elif number > array[idx]:
        return binsearch_array(number, array, idx, end)

def array_search_shit():
    array = [0, 1, 2, 3, 4, 5, 6]
    print(binsearch_array(5, array, 0, len(array)))

# with python methods
# actually does intersect
def string_intersect():
    a = "abcde"
    b = "whatever"
    c = set(a) & set(b)
    d = set(a) - c
    print(d)

# linkedlist
class lNode():
    def __init__(self, value):
        self.next = None
        self.value = value

# reverses linkedlist iteratively
def rev_linkedlist_iter():
    node1 = lNode(1)
    node2 = lNode(2)
    node1.next = node2
    node3 = lNode(3)
    node2.next = node3

    head = node1
    prev = None
    while(1):
        next = head.next
        head.next = prev
        prev = head
        if next == None:
            print("Done")
            break
        head = next

    cur = node3
    while(cur != None):
        print(cur.value)
        cur = cur.next

def rev_ll():
    node1 = lNode(1)
    node2 = lNode(2)
    node1.next = node2
    node3 = lNode(3)
    node2.next = node3
    head = revll_recur(node1)
    while head:
        print(head.value)
        head = head.next

#reverse it recursively
def revll_recur(cur):
    if cur.next == None or cur == None:
        return cur
    r = revll_recur(cur.next)
    cur.next.next = cur
    cur.next = None
    return r

# merge 2 sorted arrays
def merge_sorted(a, b):
    ai = 0
    bi = 0
    c = []
    while(a or b):
        if not a:
            for i in b:
                c.append(i)
            return c
        if not b:
            for i in a:
                c.append(i)
            return c

        elif a[0] == b[0]:
            c.append(a[0])
            a = a[1:]
            b = b[1:]
        elif a[0] < b[0]:
            c.append(a[0])
            a = a[1:]
        else:
            c.append(b[0])
            b = b[1:]
    return c

def merge():
    a = [1, 2, 4, 5, 6, 7]
    b = [3, 8, 9, 10]
    print(merge_sorted(a, b))
    print (a)
    print (b)

"""
LRU cache in java:
public class Cache extends LinkedHashMap {
    private final int cap

    public Cache(int cap) {
        super(cap + 1, 1.1, true);
        this.cap = cap;
    }

    protected boolean removeEldestEntry(Entry eldest) {
        return size() > capacity;
    }
}


"""

# Given a binary tree described by the class:

class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right

        self.value = value


#do BFS
def BFS(root, q, path):
    #add the children of the current node to the queue
    q.append(root.left)
    q.append(root.right)
    #update the path dictionary
    path[root.right] = root
    path[root.left] = root
    #pop next item in the queue, and continue
    next = q.pop(0)
    BFS(next, q, path)

#find the lowest common ancestor for a, b and root
def find_lowest(a, b, root):
    #empty dict
    path = {}
    #dictionary : {node: parent}
    path[root] = None
    #queue for BFS
    q = [] # collection.deque()
    q.append(root)
    # O(n)
    BFS(root, q, path)
    path1 = []
    path2 = []
    #build path from a to the root
    while a:
        path1.append(path[a])
        a = path[a]
    
    #build path from b
    while b:
        path2.append(path[b])
        b = path[b]
    
    #go through path 1, first common node should be lowest ancestor
    #O(logn * logn)
    for i in path1:
        if i in path2:
            return i

# Write a function that finds the lowest common ancestor of two nodes, given the two nodes and the root of the tree.
#       o
#      / \
#     o   o <- c
#        / \
#       a   o
#          / \
#             b

# a = {}
# a["b"] = "c"
# print(a)

# picture a keypad with A: 1, 2, 3 etc (phone), make all the words with 3 digits
def keypad(a, b, c):
    pad = [[1, 2, 3], ["a", "b", "c"], [4, 5, 6]]
    if a > len(pad) or b > len(pad) or c > len(pad):
        print("Out of bounds")
        return None
    for i in pad[a]:
        for j in pad[b]:
            for k in pad[c]:
                print(str(i) + j + str(k))

thing = {}
thing[1] = 2

# check if a string is a palindrome
def string_palindrome(num):
    str_num = str(num)
    for i in range(len(str_num)//2):
        if str_num[i] != str_num[:-i]:
            return False
    return True

# gets the nth to last item in a linkedlist

def nth_to_last(n, head):
    ret = head
    for i in range(n):
        head = head.next
    while head.next:
        head = head.next
        ret = ret.next
    return ret

def prep_nth():
    node0 = lNode(0)
    node1 = lNode(1)
    node0.next = node1
    node2 = lNode(2)
    node1.next = node2
    node3 = lNode(3)
    node2.next = node3
    node4 = lNode(4)
    node3.next = node4
    print(nth_to_last(1, node0).value)

def int_to_string(number):
    FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
    SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
    OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
    HUNDRED = "hundred"
    sec = False
    #if it's between 10 and 19, then it's in second 10
    if (number % 100) < 20 and (number % 100) >= 10:
        sec = True
    str_num = str(number)
    ret = ""
    for i in range(0, len(str_num)):
        if i == 0 and not sec and number%10 != 0:
            ret = FIRST_TEN[number%10-1]
        elif i == 1 and sec:
            ret = SECOND_TEN[number%10]
        elif i == 1 and not sec and number%100//10 > 1:
            ret = OTHER_TENS[number%100//10-2] + " " + ret
        elif i == 2:
            ret = FIRST_TEN[number//100-1] + " " + HUNDRED + " " + ret

# check if 2 linked lists are merged
# just check if the last node is the same...
def merged_ll(head1, head2):
    while head1.next:
        head1 = head1.next
    while head2.next:
        head2 = head2.next
    if head1 == head2:
        return True
    else:
        return False

# not sure if this works? untested
# logic should be fine... add all nodes of one LL into a map
# go through 2nd LL, return at first hit, else return None
def mergepoint(head1, head2):
    node_map = {head1 : None}
    while head1.next:
        head1 = head1.next
        node_map[head1] = head1.next
    while head2.next:
        try:
            node_map[head2]
            return head2
        except:
            continue
        head2 = head2.next
    return None

# gives intersection of 2 sorted lists in O(n)
# basically merging part of mergesort
def intersect_sorted(l1, l2):
    p1 = 0
    p2 = 0
    len1 = len(l1)
    len2 = len(l2)
    ret = []
    while p1 < len1 and p2 < len2:
        if l1[p1] == l2[p2]:
            ret.append(l1[p1])
            p1 += 1
            p2 += 1
        elif l1[p1] < l2[p2]:
            p1 += 1
        else:
            p2 += 1
    return ret
